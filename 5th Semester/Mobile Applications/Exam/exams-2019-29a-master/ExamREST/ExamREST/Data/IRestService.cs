using System.Collections.Generic;
using System.Threading.Tasks;

namespace ExamREST
{
	public interface IRestService
	{
		Task<List<ExamItem>> RefreshDataAsync ();

		Task SaveExamItemAsync (ExamItem item, bool isNewItem);

		Task DeleteExamItemAsync (int id);
	}
}
