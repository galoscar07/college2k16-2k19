using System;
using System.Collections.Generic;
using Xamarin.Forms;
using Xamarin.Forms.PlatformConfiguration.AndroidSpecific;

namespace ExamREST.Views
{
    public class TabHolder : Xamarin.Forms.TabbedPage
    {
        public List<Page> Pages { get; set; }

        public TabHolder()
        {
            Title = "Exam";
            On<Xamarin.Forms.PlatformConfiguration.Android>().SetToolbarPlacement(ToolbarPlacement.Bottom);
            PopulatePages();
        }

        private void PopulatePages()
        {
            var pages = new List<Page>();
            var listPage = new FirstSectionExamItemListPage();
            var historyPage = new FirstSectionHistory
            {
                Title = "History"
            };

            pages.Add(listPage);
            pages.Add(historyPage);

            Children.Add(listPage);
            Children.Add(historyPage);

            Pages = pages;
        }
    }
}
