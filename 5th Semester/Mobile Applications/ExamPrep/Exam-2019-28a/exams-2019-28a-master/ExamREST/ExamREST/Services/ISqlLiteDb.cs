using SQLite;

namespace PersonalAgenda.Services
{
    public interface ISqlLiteDb
    {
        SQLiteAsyncConnection GetConnection();
    }
}
