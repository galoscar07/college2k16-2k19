using System;
using System.Collections.Generic;
using ExamREST.Utilits;
using Xamarin.Forms;

namespace ExamREST.Views
{
    public partial class FirstSectionExamItemListPage : ContentPage
    {
        public FirstSectionExamItemListPage()
        {
            InitializeComponent();
        }

        protected async override void OnAppearing()
        {
            base.OnAppearing();

            if (ConnectionManager.CheckConnection())
            {
                listView.ItemsSource = await App.ExamManager.GetTasksAsync();
            }
            else
            {
                while (await DisplayAlert("Error", "Currently you are offline", "Retry", "Cancel"))
                {
                    if (ConnectionManager.CheckConnection())
                    {
                        break;
                    }
                    listView.ItemsSource = await App.ExamManager.GetTasksAsync();
                }
            }

        }

        async void OnRefresh(object sender, System.EventArgs e)
        {
            listView.IsRefreshing = true;

            if (ConnectionManager.CheckConnection())
            {
                listView.ItemsSource = await App.ExamManager.GetTasksAsync();
            }
            else
            {
                while (await DisplayAlert("Error", "Currently you are offline", "Retry", "Cancel"))
                {
                    if (ConnectionManager.CheckConnection())
                    {
                        break;
                    }
                    listView.ItemsSource = await App.ExamManager.GetTasksAsync();
                }
            }
            listView.IsRefreshing = false;
        }

        //void OnAddItemClicked(object sender, EventArgs e)
        //{
        //    var examItem = new ExamItem()
        //    {
        //        Id = (int)DateTime.Now.Ticks % 1000000000
        //    };
        //    var examPage = new SecondSectionExamItemPage(true)
        //    {
        //        BindingContext = examItem
        //    };
        //    Navigation.PushAsync(examPage);
        //}

        void OnItemSelected(object sender, SelectedItemChangedEventArgs e)
        {
            var examItem = e.SelectedItem as ExamItem;
            var examPage = new FirstSectionExamItemPage();
            examPage.BindingContext = examItem;
            Navigation.PushAsync(examPage);
        }
    }
}
