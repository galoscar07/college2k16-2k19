using System;
using System.ComponentModel;
using ExamREST.Utilits;
using Xamarin.Forms;

namespace ExamREST
{
    public partial class FirstSectionExamItemPage : ContentPage, INotifyPropertyChanged
    {
        bool isNewItem;
        bool canSwitch = true;
        private bool _shouldDisplayData;
        private int idOfTheElement;

        public bool ShouldDisplayData
        {
            get { return _shouldDisplayData; }
            set
            {
                _shouldDisplayData = value;
                OnPropertyChanged(nameof(ShouldDisplayData));
            }
        }

        private string _displayText = "Use Place";

        public string DisplayText
        {
            get { return _displayText; }
            set
            {
                _displayText = value;
                OnPropertyChanged(nameof(DisplayText));
            }
        }

        private ExamItem _examItem;

        public ExamItem ExamItem
        {
            get { return _examItem; }
            set
            {
                _examItem = value;
                OnPropertyChanged(nameof(ExamItem));
            }
        }

        public FirstSectionExamItemPage(bool isNew = false)
        {
            InitializeComponent();
            isNewItem = isNew;
        }

        protected override void OnBindingContextChanged()
        {
            base.OnBindingContextChanged();

            if (BindingContext == null || BindingContext is FirstSectionExamItemPage)
            {
                return;
            }
            ExamItem = (ExamItem)BindingContext;
            BindingContext = this;
        }

        async void OnSaveActivated(object sender, EventArgs e)
        {
            var examItem = (ExamItem)BindingContext;
            await App.ExamManager.SaveTaskAsync(examItem, isNewItem);
            await Navigation.PopAsync();
        }

        async void OnDeleteActivated(object sender, EventArgs e)
        {
            var examItem = (ExamItem)BindingContext;
            await App.ExamManager.DeleteTaskAsync(examItem);
            await Navigation.PopAsync();
        }

        void OnCancelActivated(object sender, EventArgs e)
        {
            Navigation.PopAsync();
        }

        async void Handle_PropertyChanged(object sender, System.ComponentModel.PropertyChangedEventArgs e)
        {
            if (sender == null || e.PropertyName != "IsToggled" || !canSwitch)
            {
                return;
            }

            if (!ConnectionManager.CheckConnection())
            {
                while (await DisplayAlert("Error", "Currently you are offline", "Retry", "Cancel"))
                {
                    if (ConnectionManager.CheckConnection())
                    {
                        canSwitch = true;
                        break;
                    }  
                }

                if (!ConnectionManager.CheckConnection())
                {
                    canSwitch = false;
                    ((Switch)sender).IsToggled = !((Switch)sender).IsToggled;
                    return;
                }
            }

            switch (ExamItem.Status)
            {
                case "available":
                    await App.ExamManager.LoanSlotAsync(ExamItem);
                    idOfTheElement = ExamItem.Id;
                    await App.ExamManager.SaveTaskAsync(ExamItem, offline: true);
                    DisplayText = "Return Place";
                    ExamItem.Status = "taken";
                    ShouldDisplayData = true;
                    break;
                case "taken":
                    ShouldDisplayData = false;
                    DisplayText = "Loan Place";
                    ExamItem.Id = idOfTheElement;
                    await App.ExamManager.ReturnSlotAsync(ExamItem);
                    ExamItem.Status = "available";
                    break;
            }
        }

        public event PropertyChangedEventHandler PropertyChanged;

        protected void OnPropertyChanged(string propertyName)
        {
            if (PropertyChanged != null)
                PropertyChanged(this, new PropertyChangedEventArgs(propertyName));
        }
    }
}
