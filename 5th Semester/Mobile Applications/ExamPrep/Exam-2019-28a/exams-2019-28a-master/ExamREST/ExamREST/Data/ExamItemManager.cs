using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using PersonalAgenda.Services;
using System.Linq;
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

        public async Task<List<ExamItem>> GetTaskFromDatabase()
        {
            return (List<ExamItem>)await DataStore.GetAllItemsAsync();
        }

        public async Task<List<ExamItem>> GetTasksAsync (bool hasOfflineSupport = false, string status = "available")
		{
            if (hasOfflineSupport)
            {
                var tempList = await restService.RefreshDataAsync();

                if (tempList.Count <= 0)
                {
                    return (List<ExamItem>)await DataStore.GetAllItemsAsync();
                }
                return tempList.Where((item) => item.Status == status).ToList();
            }
            return (await restService.RefreshDataAsync ()).Where((item) => item.Status == status).ToList();	
		}

        public Task SaveTaskAsync (ExamItem item, bool isNewItem = false, bool offline = false)
		{
            return offline ? DataStore.AddItemAsync(item) : restService.SaveExamItemAsync (item, isNewItem);
        }

        public Task DeleteTaskAsync (ExamItem item)
		{
            return restService.DeleteExamItemAsync(item.Id);
		}

        public Task LoanSlotAsync(ExamItem item)
        {
            return restService.LoanSlotAsync(item.Id);
        }

        public Task ReturnSlotAsync(ExamItem item)
        {
            return restService.ReturnSlotAsync(item.Id);
        }

        public async Task<List<ExamItem>> GetAllTasksAsync ()
        {
            var tempList = await restService.GetAllTasks();
            return tempList.OrderByDescending(item=>item.Status).ThenByDescending(item => item.Power).ToList();
        }
    }
}
