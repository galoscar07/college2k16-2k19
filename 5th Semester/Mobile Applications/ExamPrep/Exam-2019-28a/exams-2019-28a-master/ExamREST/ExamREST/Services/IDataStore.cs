using System;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace PersonalAgenda.Services
{
    public interface IDataStore<T>
    {
        Task<bool> AddItemAsync(T item);
        Task<bool> UpdateItemAsync(T item);
        Task<bool> DeleteItemAsync(int id);
        Task<T> GetItemAsync<P>(int id, P filter);
        Task<IEnumerable<T>> GetItemsAsync<P>(P filter, bool forceRefresh = false);
        Task<ICollection<T>> GetAllItemsAsync();
        Task ReinitializeStorageAsync(ICollection<T> source);
    }
}
