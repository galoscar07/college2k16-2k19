using System;
using System.Collections.Generic;
using System.Data.Entity;
using System.Linq;
using System.Web;

namespace ProiectColectiv.Models.Domain
{
    public class SchoolContext : DbContext
    {
        public DbSet<Attendance> Attendances { get; set; }
        public DbSet<Student> Students { get; set; }
        public DbSet<Subject> Subjects { get; set; }
        public DbSet<Teacher> Teachers { get; set; }
		public DbSet<Credential> Credentials { get; set; }
		public DbSet<TeacherSubject> TeacherSubjects { get; set; }

        public SchoolContext() : base("name=DbConnection")
        {
            Configuration.LazyLoadingEnabled = false;
        }

        protected override void OnModelCreating(DbModelBuilder modelBuilder)
        {
            base.OnModelCreating(modelBuilder);
        }


    }
}