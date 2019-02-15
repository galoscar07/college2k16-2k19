using System;
using System.ComponentModel;
using ExamREST.Utilits;
using Xamarin.Forms;

namespace ExamREST
{
    public partial class FirstSectionExamItemHistoryPage : ContentPage
    {
        bool isNewItem;

        public FirstSectionExamItemHistoryPage(bool isNew = false)
        {
            InitializeComponent();
            isNewItem = isNew;
        }
    }
}
