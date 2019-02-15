#include <iostream>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <vector>
#include <thread>
#include <mpi.h>

using namespace cv;
using namespace std;


inline int convertToInt(char *s) {
    string _s(s);
    stringstream str(_s);
    int x;
    str >> x;
    if(!str || x <= 0) {
        return -1;
    }
    return x;
}

inline int magic_transform(int R, int G, int B) {
    return 0.21 * R + 0.72 * G + 0.07 * B;
}

inline void apply_filters(Mat &grey_img, Mat &red_img, Mat &green_img, Mat &blue_img, int st, int fn, int me) {
        cerr << "> proc " << me << " applying black & white filter\n";
        for (int i = st; i < fn; ++i) {
            for (int j = 0; j < grey_img.cols; ++j) {
                Vec3b px = grey_img.at<Vec3b>(i, j);
                int magic = magic_transform(px[0], px[1], px[2]);
                px[0] = magic;
                px[1] = magic;
                px[2] = magic;
                grey_img.at<Vec3b>(i, j) = px;
            }
        }
        cerr << "> proc " << me << " applied black & white filter\n";

        cerr << "> proc " << me << " applying red saturation filter\n";
        for (int i = st; i < fn; ++i) {
            for (int j = 0; j < red_img.cols; ++j) {
                Vec3b px = red_img.at<Vec3b>(i, j);
                px[0] *= 0.1;
                px[1] *= 0.1;
                red_img.at<Vec3b>(i, j) = px;
            }
        }
        cerr << "> proc " << me << " applied red saturation filter\n";

        cerr << "> proc " << me << " applying green saturation filter\n";
        for (int i = st; i < fn; ++i) {
            for (int j = 0; j < green_img.cols; ++j) {
                Vec3b px = green_img.at<Vec3b>(i, j);
                px[0] *= 0.1;
                px[2] *= 0.1;
                green_img.at<Vec3b>(i, j) = px;
            }
        }
        cerr << "> proc " << me << " applied green saturation filter\n";

        cerr << "> proc " << me << " applying blue saturation filter\n";
        for (int i = st; i < fn; ++i) {
            for (int j = 0; j < blue_img.cols; ++j) {
                Vec3b px = blue_img.at<Vec3b>(i, j);
                px[1] *= 0.1;
                px[2] *= 0.1;
                blue_img.at<Vec3b>(i, j) = px;
            }
        }
        cerr << "> proc " << me << " applied blue saturation filter\n";
}

inline void collect(Mat &grey_img, Mat &red_img, Mat &green_img, Mat &blue_img, int nrProcs) {
    cerr << "> master collects data";
    int rows = grey_img.rows;
    int cols = grey_img.cols;
    MPI_Status _;
    for (int i = 1; i < nrProcs; ++ i) {
        int st = i * rows / nrProcs;
        int dr = (i + 1) * rows / nrProcs;
        MPI_Recv(grey_img.rowRange(st, dr).data, (dr - st) * cols * 3, MPI_BYTE, i, 3, MPI_COMM_WORLD, &_);
        MPI_Recv(red_img.rowRange(st, dr).data, (dr - st) * cols * 3, MPI_BYTE, i, 3, MPI_COMM_WORLD, &_);
        MPI_Recv(green_img.rowRange(st, dr).data, (dr - st) * cols * 3, MPI_BYTE, i, 3, MPI_COMM_WORLD, &_);
        MPI_Recv(blue_img.rowRange(st, dr).data, (dr - st) * cols * 3, MPI_BYTE, i, 3, MPI_COMM_WORLD, &_);
    }
    cerr << "> master collected data";
}

inline void master(Mat &grey_img, Mat &red_img, Mat &green_img, Mat &blue_img, int nrProcs) {
    cerr << "> master sending work to slaves\n";
    int rows = grey_img.rows;
    int cols = grey_img.cols;
    for (int i = 1; i < nrProcs; ++ i) {
        int st = i * rows / nrProcs;
        int dr = min(rows, (i + 1) * rows / nrProcs);
        int nr_rows = dr - st;
        MPI_Bsend(&nr_rows, 1, MPI_INT, i, 0, MPI_COMM_WORLD);
        MPI_Bsend(&cols, 1, MPI_INT, i, 1, MPI_COMM_WORLD);
        MPI_Ssend(grey_img.rowRange(st, dr).data, nr_rows * cols * 3, MPI_BYTE, i, 2, MPI_COMM_WORLD);
        MPI_Ssend(red_img.rowRange(st, dr).data, nr_rows * cols * 3, MPI_BYTE, i, 2, MPI_COMM_WORLD);
        MPI_Ssend(green_img.rowRange(st, dr).data, nr_rows * cols * 3, MPI_BYTE, i, 2, MPI_COMM_WORLD);
        MPI_Ssend(blue_img.rowRange(st, dr).data, nr_rows * cols * 3, MPI_BYTE, i, 2, MPI_COMM_WORLD);
    }
    apply_filters(grey_img, red_img, green_img, blue_img, 0, rows / nrProcs, 0);
    collect(grey_img, red_img, green_img, blue_img, nrProcs);
    cerr << "> master sent work to slaves\n";
}

inline void slave(int me) {
    cerr << "> slave " << me << " started\n";
    int n, m;
    MPI_Status _;
    MPI_Recv(&n, 1, MPI_INT, 0, 0, MPI_COMM_WORLD, &_);
    MPI_Recv(&m, 1, MPI_INT, 0, 1, MPI_COMM_WORLD, &_);
    Mat chunk1(n, m, CV_8UC3);
    Mat chunk2(n, m, CV_8UC3);
    Mat chunk3(n, m, CV_8UC3);
    Mat chunk4(n, m, CV_8UC3);
    MPI_Recv(chunk1.data, n * m * 3, MPI_BYTE, 0, 2, MPI_COMM_WORLD, &_);
    MPI_Recv(chunk2.data, n * m * 3, MPI_BYTE, 0, 2, MPI_COMM_WORLD, &_);
    MPI_Recv(chunk3.data, n * m * 3, MPI_BYTE, 0, 2, MPI_COMM_WORLD, &_);
    MPI_Recv(chunk4.data, n * m * 3, MPI_BYTE, 0, 2, MPI_COMM_WORLD, &_);
    apply_filters(chunk1, chunk2, chunk3, chunk4, 0, n, me);
    MPI_Ssend(chunk1.data, n * m * 3, MPI_BYTE, 0, 3, MPI_COMM_WORLD);
    MPI_Ssend(chunk2.data, n * m * 3, MPI_BYTE, 0, 3, MPI_COMM_WORLD);
    MPI_Ssend(chunk3.data, n * m * 3, MPI_BYTE, 0, 3, MPI_COMM_WORLD);
    MPI_Ssend(chunk4.data, n * m * 3, MPI_BYTE, 0, 3, MPI_COMM_WORLD);
    cerr << "> slave finished\n";
}

int main(int argc, char** argv ) {
    srand(time(NULL));
    MPI_Init(0, 0);

    // get the current process id & the avaialble number of nodes
    int me;
    int nrProcs;
    MPI_Comm_size(MPI_COMM_WORLD, &nrProcs);
    MPI_Comm_rank(MPI_COMM_WORLD, &me);
    cout << me << endl;

    // check the current time
    clock_t t;
    t = clock();

    if (argc != 2) {
        printf("Usage: Filters.o <Image_Path>\n");
        return -1;
    }

    if(me == 0) {
        string filename = argv[1];
        Mat gray_scale_image, blue_saturated_image, green_saturated_image, red_saturated_image;
        if (argc == 2) {
            gray_scale_image = imread(argv[1], IMREAD_COLOR);
            blue_saturated_image = imread(argv[1], IMREAD_COLOR);
            green_saturated_image = imread(argv[1], IMREAD_COLOR);
            red_saturated_image = imread(argv[1], IMREAD_COLOR);
            if (!gray_scale_image.data || !blue_saturated_image.data || !green_saturated_image.data || !red_saturated_image.data) {
                printf("No image data\n");
                return -1;
            }
        }
        master(gray_scale_image, red_saturated_image, green_saturated_image, blue_saturated_image, nrProcs);
        imwrite("output/grayscale.jpg", gray_scale_image);
        imwrite("output/blue_saturated.jpg", blue_saturated_image);
        imwrite("output/green_saturated.jpg", green_saturated_image);
        imwrite("output/red_saturated.jpg", red_saturated_image);

        // get the total time took to perform the operations
        t = clock() - t;
        cout << "Applying filters to an image of "
             << gray_scale_image.rows << "x" << gray_scale_image.cols << " with " << nrProcs
             << " nodes took me " << t << " cycles ("
             << static_cast<float> (t) / CLOCKS_PER_SEC << " seconds)\n";

        cout << "Generated images saved in the output directory\n";
    } else {
        slave(me);
    }
    MPI_Finalize();
    return 0;
}
