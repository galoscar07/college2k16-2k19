using System;
using System.Collections.Generic;

using Xamarin.Forms;

namespace ExamREST.Views
{
    public partial class ChooseSection : ContentPage
    {
        public ChooseSection()
        {
            InitializeComponent();
        }

        void FirstSectionClicked(object sender, System.EventArgs e)
        {
            Application.Current.MainPage.Navigation.PushAsync(new TabHolder());
        }

        void SecondSectionClicked(object sender, System.EventArgs e)
        {
            Application.Current.MainPage.Navigation.PushAsync(new SecondSectionExamListPage());
        }
    }
}
