using Xamarin.Forms;

namespace ExamREST.Views
{
    public partial class FirstSectionHistory : ContentPage
    {
        public FirstSectionHistory()
        {
            InitializeComponent();
        }

        protected async override void OnAppearing()
        {
            base.OnAppearing();

            listView.ItemsSource = await App.ExamManager.GetTasksAsync(hasOfflineSupport: true);
        }

        async void OnRefresh(object sender, System.EventArgs e)
        {
            listView.IsRefreshing = true;
            listView.ItemsSource = await App.ExamManager.GetTasksAsync(hasOfflineSupport: true);
            listView.IsRefreshing = false;
        }
    }
}
