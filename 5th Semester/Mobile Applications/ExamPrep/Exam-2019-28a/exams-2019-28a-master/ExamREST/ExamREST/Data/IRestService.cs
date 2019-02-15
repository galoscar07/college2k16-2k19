using System.Collections.Generic;
using System.Threading.Tasks;

namespace ExamREST
{
	public interface IRestService
	{
		Task<List<ExamItem>> RefreshDataAsync ();

		Task SaveExamItemAsync (ExamItem item, bool isNewItem);

		Task DeleteExamItemAsync (int id);

        Task LoanSlotAsync(int id);

        Task ReturnSlotAsync(int id);

        Task<List<ExamItem>> GetAllTasks();
    }
}
