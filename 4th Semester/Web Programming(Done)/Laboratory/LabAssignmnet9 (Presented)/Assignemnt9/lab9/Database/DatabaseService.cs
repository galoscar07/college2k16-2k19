using System;
using System.Collections.Generic;
using lab9.Models;
using MySql.Data.MySqlClient;
using Newtonsoft.Json;

namespace lab9.Database
{
    public class DatabaseService
    {
        static MySqlConnection conn = new MySqlConnection
        {
            ConnectionString = "server=localhost;uid=root;pwd=;database=dest;port=3306;SslMode=none;"
        };

        public static int AddUser(User user, string password)
        {
            int result;
			try
			{
				conn.Open();
				MySqlCommand cmd = new MySqlCommand();
				cmd.Connection = conn;
				cmd.CommandText = string.Format("insert into users (email, password, name) values " +
                                                "('{0}', '{1}', '{2}')", user.Email, password, user.Name);
                int affected = cmd.ExecuteNonQuery();
                if (affected > 0)
                {
                    cmd.Parameters.Add(new MySqlParameter("newId", cmd.LastInsertedId));
                    result = Convert.ToInt32(cmd.Parameters["@newId"].Value);
                }
                else
                {
                    result = 0;
                }
                conn.Close();
				return result;
			}
			catch (MySqlException ex)
			{
				Console.Write(ex.Message);
				conn.Close();
                return 0;
			}
        }

		public static User GetUser(string email, string password)
		{
            User user = null;
			try
            {
				conn.Open();
				MySqlCommand cmd = new MySqlCommand();
				cmd.Connection = conn;
                cmd.CommandText = "select * from users where email='" + email + "' and password='" + password + "'";
                MySqlDataReader myreader = cmd.ExecuteReader();
				while (myreader.Read())
				{
                    user = new User(myreader.GetString("email"), 
                                    myreader.GetString("name"), myreader.GetInt32("id"));
				}
				myreader.Close();
                conn.Close();
			}
			catch (MySqlException ex)
			{
				Console.Write(ex.Message);
                conn.Close();
			}
            return user;
		}

        public static string GetDestination(string country = "")
        {
            List<Destination> dests = new List<Destination>();
			try
			{
				conn.Open();
				MySqlCommand cmd = new MySqlCommand();
				cmd.Connection = conn;
                country = "%" + country + "%";
                cmd.CommandText = "select * from dest where country like '" + country + "'";
				MySqlDataReader myreader = cmd.ExecuteReader();
				while (myreader.Read())
				{
                    Destination dest = new Destination(myreader.GetString("city"), myreader.GetString("country"), myreader.GetString("description"),
                                                       myreader.GetInt32("tourist"), myreader.GetInt32("cost"));
                    dest.Id = myreader.GetInt32("id");
                    dests.Add(dest);
				}
				myreader.Close();
				conn.Close();
			}
			catch (MySqlException ex)
			{
				Console.Write(ex.Message);
				conn.Close();
			}
            return JsonConvert.SerializeObject(dests);
        }

        public static Destination GetDestinationById(int id)
        {
            Destination dest = new Destination();
            try
            {
                conn.Open();
                MySqlCommand cmd = new MySqlCommand();
                cmd.Connection = conn;
                cmd.CommandText = "select * from dest where id='" + id + "'";
                MySqlDataReader myreader = cmd.ExecuteReader();
                while (myreader.Read())
				{
                    dest = new Destination(myreader.GetString("city"), myreader.GetString("country"), myreader.GetString("description"),
                                           myreader.GetInt32("tourist"), myreader.GetInt32("cost"));
                    dest.Id = myreader.GetInt32("id");
                }
                myreader.Close();
                conn.Close();
            }
			catch (MySqlException ex)
			{
				Console.Write(ex.Message);
				conn.Close();
			}
            return dest;
        }

        public static void AddDestination(Destination dest)
        {
			try
			{
				conn.Open();
				MySqlCommand cmd = new MySqlCommand();
				cmd.Connection = conn;
                cmd.CommandText = string.Format("insert into dest (city, country, description, tourist, cost) values " +
                                                "({0})", dest);
                cmd.ExecuteNonQuery();
            }
			catch (MySqlException ex)
			{
				Console.Write(ex.Message);
				conn.Close();
			}
            conn.Close();
        }

        public static void DeleteDestination(int id)
        {
			try
			{
				conn.Open();
				MySqlCommand cmd = new MySqlCommand();
				cmd.Connection = conn;
                cmd.CommandText = "delete from dest where id='" + id + "'";
				cmd.ExecuteNonQuery();
			}
			catch (MySqlException ex)
			{
				Console.Write(ex.Message);
				conn.Close();
			}
			conn.Close();
        }

        public static void UpdateDestination(Destination dest)
        {
			try
			{
				conn.Open();
				MySqlCommand cmd = new MySqlCommand();
				cmd.Connection = conn;
                cmd.CommandText = string.Format("update dest set city='{0}', country='{1}', description='{2}', tourist='{3}'," +
                                                " cost='{4}' where id={5}", dest.City, dest.Country, dest.Description,
                                                dest.Tourist, dest.Cost, dest.Id);
				cmd.ExecuteNonQuery();
			}
			catch (MySqlException ex)
			{
				Console.Write(ex.Message);
				conn.Close();
			}
			conn.Close();
        }
    }
}
