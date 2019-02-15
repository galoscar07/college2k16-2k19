using System;
using System.IO;
using PersonalAgenda.Droid.Services;
using PersonalAgenda.Services;
using SQLite;
using Xamarin.Forms;

[assembly: Dependency(typeof(SqlLiteDb))]
namespace PersonalAgenda.Droid.Services
{
    public class SqlLiteDb : ISqlLiteDb
    {
        public SQLiteAsyncConnection GetConnection()
        {
            var documentsPath = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments);
            var path = Path.Combine(documentsPath, "Exam.db3");

            return new SQLiteAsyncConnection(path);
        }
    }
}
