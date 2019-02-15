namespace lab9.Models
{
    public class User
    {
        public string Email { get; set; }
        public string Name { get; set; }
        public int Id { get; set; }

        public User() {}

        public User(string email, string name, int id = 0)
        {
            Email = email;
            Name = name;
            Id = id;
        }
    }
}
