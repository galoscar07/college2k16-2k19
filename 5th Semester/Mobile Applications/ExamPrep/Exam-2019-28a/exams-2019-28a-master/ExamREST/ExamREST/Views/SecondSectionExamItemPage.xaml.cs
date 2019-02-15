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

		async void OnDeleteActivated (object sender, EventArgs e)
		{
			var examItem = (ExamItem)BindingContext;
			await App.ExamManager.DeleteTaskAsync (examItem);
			await Navigation.PopAsync ();
		}
	}
}
