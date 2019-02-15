using System;
using Xamarin.Forms;

namespace ExamREST
{
	public partial class SecondSectionExamListPage : ContentPage
	{
		public SecondSectionExamListPage ()
		{
			InitializeComponent ();
		}

		protected async override void OnAppearing ()
		{
			base.OnAppearing ();

			listView.ItemsSource = await App.ExamManager.GetAllTasksAsync ();
		}

        async void OnRefresh(object sender, System.EventArgs e)
        {
            listView.IsRefreshing = true;
            listView.ItemsSource = await App.ExamManager.GetAllTasksAsync();
            listView.IsRefreshing = false;
        }

        void OnAddItemClicked (object sender, EventArgs e)
		{
			var examItem = new ExamItem () {
				Id = (int)DateTime.Now.Ticks % 1000000000
			};
            var examPage = new SecondSectionExamItemPage(true)
            {
                BindingContext = examItem
            };
            Navigation.PushAsync (examPage);
		}

		void OnItemSelected (object sender, SelectedItemChangedEventArgs e)
		{
			var examItem = e.SelectedItem as ExamItem;
			var examPage = new SecondSectionExamItemPage ();
            examPage.BindingContext = examItem;
			Navigation.PushAsync (examPage);
		}
	}
}
