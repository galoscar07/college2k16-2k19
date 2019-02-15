using System;
using ExamREST.Views;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;

[assembly: XamlCompilation(XamlCompilationOptions.Compile)]
namespace ExamREST
{
    public partial class App : Application
    {
        public static ExamItemManager ExamManager { get; private set; }

        public App()
        {
            InitializeComponent();

            ExamManager = new ExamItemManager(new RestService());
            MainPage = new NavigationPage(new ChooseSection());
        }

        protected override void OnStart()
        {
            // Handle when your app starts
        }

        protected override void OnSleep()
        {
            // Handle when your app sleeps
        }

        protected override void OnResume()
        {
            // Handle when your app resumes
        }
    }
}
