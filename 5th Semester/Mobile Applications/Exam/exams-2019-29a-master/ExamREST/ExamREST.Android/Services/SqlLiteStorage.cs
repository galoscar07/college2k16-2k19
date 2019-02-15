using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using ExamREST;
using PersonalAgenda.Droid.Services;
using PersonalAgenda.Services;
using SQLite;
using Xamarin.Forms;
using Xamarin.Forms.Internals;

[assembly: Dependency(typeof(SqlLiteStorage))]
namespace PersonalAgenda.Droid.Services
{
    public class SqlLiteStorage : IDataStore<ExamItem>
    {
        private SQLiteAsyncConnection _connection;

        public SqlLiteStorage()
        {
            _connection = DependencyService.Get<ISqlLiteDb>().GetConnection();
            _connection.CreateTableAsync<ExamItem>();
        }

        public async Task<bool> AddItemAsync(ExamItem item)
        {
            item.Id = (int)DateTime.Now.Ticks % 1000000000;
            await _connection.InsertAsync(item);

            return await Task.FromResult(true);
        }

        public async Task<bool> UpdateItemAsync(ExamItem item)
        {
            await _connection.UpdateAsync(item);

            return await Task.FromResult(true);
        }

        public async Task<bool> DeleteItemAsync(int id)
        {
            await _connection.DeleteAsync<ExamItem>(id);

            return await Task.FromResult(true);
        }

        public async Task<ExamItem> GetItemAsync<T>(int id, T filter)
        {
            return filter == null
                ? await _connection.Table<ExamItem>().FirstOrDefaultAsync((it) => it.Id.Equals(id))
                : await _connection.Table<ExamItem>().FirstOrDefaultAsync((it) => it.Id.Equals(id) && it.Date.Equals(filter));
        }

        public async Task<IEnumerable<ExamItem>> GetItemsAsync<T>(T filter, bool forceRefresh = false)
        {
            return await _connection.Table<ExamItem>().Where((it) => it.Date.Equals(filter)).ToListAsync();
        }

        public async Task<ICollection<ExamItem>> GetAllItemsAsync()
        {
            return await _connection.Table<ExamItem>().ToListAsync();
        }

        public async Task ReinitializeStorageAsync(ICollection<ExamItem> source)
        {
            await _connection.DropTableAsync<ExamItem>();
            await _connection.CreateTableAsync<ExamItem>();
            source.ForEach(async (ev) => await AddItemAsync(ev));
        }
    }
}
