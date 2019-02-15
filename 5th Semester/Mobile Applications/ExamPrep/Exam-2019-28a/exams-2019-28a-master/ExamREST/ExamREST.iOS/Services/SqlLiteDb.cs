using System;
using System.IO;
using PersonalAgenda.iOS.Services;
using PersonalAgenda.Services;
using SQLite;
using Xamarin.Forms;

[assembly: Dependency(typeof(SqlLiteDb))]
namespace PersonalAgenda.iOS.Services
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
