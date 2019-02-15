#include <iostream>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <vector>
#include <thread>

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

int main(int argc, char** argv ) {
    clock_t t;
    t = clock();
    if (argc != 3) {
        printf("Usage: Filters.o <Image_Path> <Number_of_threads>\n");
        return -1;
    }
    string filename = argv[1];
    int N;
    int T = convertToInt(argv[2]);
    if(T == -1) {
        printf("Please give me a valid integer for the number of threads\n");
        return -1;
    }
    T *= 4;
    Mat gray_scale_image, blue_saturated_image, green_saturated_image, red_saturated_image;
    if (argc == 3) {
        printf("Applying filters to %s\n", filename.c_str());
        gray_scale_image = imread(argv[1], IMREAD_COLOR);
        blue_saturated_image = imread(argv[1], IMREAD_COLOR);
        green_saturated_image = imread(argv[1], IMREAD_COLOR);
        red_saturated_image = imread(argv[1], IMREAD_COLOR);
        if (!gray_scale_image.data || !blue_saturated_image.data || !green_saturated_image.data || !red_saturated_image.data) {
            printf("No image data\n");
            return -1;
        }
    }
    printf("Started working...\n");
    vector <thread> th;
    for(int t = 0; t < min(gray_scale_image.rows, T); ++ t) {
        th.push_back(thread([&gray_scale_image, t, T](){
            for(int i = t; i < gray_scale_image.rows; i += T) {
                for(int j = 0; j < gray_scale_image.cols; ++ j) {
                    Vec3b px = gray_scale_image.at<Vec3b>(i, j);
                    int gray = (px[0] + px[1] + px[2]) / 3;
                    px[0] = gray;
                    px[1] = gray;
                    px[2] = gray;
                    gray_scale_image.at<Vec3b>(i, j) = px;
                }
            }
        }));
        th.push_back(thread([&blue_saturated_image, t, T]() {
            for (int i = t; i < blue_saturated_image.rows; i += T) {
                for (int j = 0; j < blue_saturated_image.cols; ++j) {
                    Vec3b px = blue_saturated_image.at<Vec3b>(i, j);
                    px[1] *= 0.1;
                    px[2] *= 0.1;
                    blue_saturated_image.at<Vec3b>(i, j) = px;
                }
            }
        }));
        th.push_back(thread([&green_saturated_image, t, T]() {
            for (int i = t; i < green_saturated_image.rows; i += T) {
                for (int j = 0; j < green_saturated_image.cols; ++j) {
                    Vec3b px = green_saturated_image.at<Vec3b>(i, j);
                    px[0] *= 0.1;
                    px[2] *= 0.1;
                    green_saturated_image.at<Vec3b>(i, j) = px;
                }
            }
        }));
        th.push_back(thread([&red_saturated_image, t, T]() {
            for (int i = t; i < red_saturated_image.rows; i += T) {
                for (int j = 0; j < red_saturated_image.cols; ++j) {
                    Vec3b px = red_saturated_image.at<Vec3b>(i, j);
                    px[0] *= 0.1;
                    px[1] *= 0.1;
                    red_saturated_image.at<Vec3b>(i, j) = px;
                }
            }
        }));
    }
    for(int i = 0; i < th.size(); ++ i) {
        th[i].join();
    }
    imwrite("output/grayscale.jpg", gray_scale_image);
    imwrite("output/blue_saturated.jpg", blue_saturated_image);
    imwrite("output/green_saturated.jpg", green_saturated_image);
    imwrite("output/red_saturated.jpg", red_saturated_image);
    t = clock() - t;
    cout << "Applying filters to an image of "
         << gray_scale_image.rows << "x" << gray_scale_image.cols << " with " << T
         << " threads took me " << t << " cycles ("
         << static_cast<float> (t) / CLOCKS_PER_SEC << " seconds)\n";
    cout << "Generated images saved in the output directory\n";
    return 0;
}
