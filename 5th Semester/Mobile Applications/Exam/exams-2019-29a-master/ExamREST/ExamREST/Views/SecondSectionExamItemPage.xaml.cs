using System;
using Xamarin.Forms;

namespace ExamREST
{
	public partial class SecondSectionExamItemPage : ContentPage
	{
		bool isNewItem;

		public SecondSectionExamItemPage (bool isNew = false)
		{
			InitializeComponent ();
			isNewItem = isNew;
		}

		async void OnSaveActivated (object sender, EventArgs e)
		{
			var examItem = (ExamItem)BindingContext;
			await App.ExamManager.SaveTaskAsync (examItem, isNewItem);
			await Navigation.PopAsync ();
		}

		async void OnDeleteActivated (object sender, EventArgs e)
		{
			var examItem = (ExamItem)BindingContext;
			await App.ExamManager.DeleteTaskAsync (examItem);
			await Navigation.PopAsync ();
		}

		void OnCancelActivated (object sender, EventArgs e)
		{
			Navigation.PopAsync ();
		}
	}
}
