using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using PersonalAgenda.Services;
using Xamarin.Forms;

namespace ExamREST
{
	public class ExamItemManager
	{
		IRestService restService;
        public static IDataStore<ExamItem> DataStore = DependencyService.Get<IDataStore<ExamItem>>();

        public ExamItemManager (IRestService service)
		{
			restService = service;
		}

		public async Task<List<ExamItem>> GetTasksAsync (bool hasOfflineSupport = false)
		{
            if (hasOfflineSupport)
            {
                var tempList = await restService.RefreshDataAsync();

                if (tempList.Count <= 0)
                {
                    return (List<ExamItem>)await DataStore.GetAllItemsAsync();
                }
                return tempList;
            }
            return await restService.RefreshDataAsync ();	
		}

		public Task SaveTaskAsync (ExamItem item, bool isNewItem = false)
		{
			return restService.SaveExamItemAsync (item, isNewItem);
		}

		public Task DeleteTaskAsync (ExamItem item)
		{
			return restService.DeleteExamItemAsync (item.Id);
		}
	}
}
