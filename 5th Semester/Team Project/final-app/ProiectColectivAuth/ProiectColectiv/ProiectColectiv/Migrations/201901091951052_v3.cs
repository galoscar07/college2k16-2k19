namespace ProiectColectiv.Migrations
{
    using System;
    using System.Data.Entity.Migrations;
    
    public partial class v3 : DbMigration
    {
        public override void Up()
        {
            DropPrimaryKey("dbo.TeacherSubjects");
            AddColumn("dbo.TeacherSubjects", "id", c => c.Long(nullable: false, identity: true));
            AddPrimaryKey("dbo.TeacherSubjects", "id");
        }
        
        public override void Down()
        {
            DropPrimaryKey("dbo.TeacherSubjects");
            DropColumn("dbo.TeacherSubjects", "id");
            AddPrimaryKey("dbo.TeacherSubjects", new[] { "GroupID", "SubGroup" });
        }
    }
}
