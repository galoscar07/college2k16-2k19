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

            listView.ItemsSource = await App.ExamManager.GetTaskFromDatabase();
        }

        async void OnRefresh(object sender, System.EventArgs e)
        {
            listView.IsRefreshing = true;
            listView.ItemsSource = await App.ExamManager.GetTaskFromDatabase();
            listView.IsRefreshing = false;
        }

        void OnItemSelected(object sender, SelectedItemChangedEventArgs e)
        {
            var examItem = e.SelectedItem as ExamItem;
            var examPage = new FirstSectionExamItemHistoryPage();
            examPage.BindingContext = examItem;
            Navigation.PushAsync(examPage);
        }
    }
}
