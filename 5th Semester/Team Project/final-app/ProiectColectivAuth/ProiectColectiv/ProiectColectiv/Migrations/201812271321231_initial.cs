namespace ProiectColectiv.Migrations
{
    using System;
    using System.Data.Entity.Migrations;
    
    public partial class initial : DbMigration
    {
        public override void Up()
        {
            CreateTable(
                "dbo.Attendances",
                c => new
                    {
                        WeekNumber = c.Int(nullable: false),
                        Type = c.String(nullable: false, maxLength: 128),
                        StudentID = c.Long(nullable: false),
                        TeacherID = c.Long(nullable: false),
                        SubjectID = c.Long(nullable: false),
                        grade = c.Int(),
                        TimeStamp = c.Binary(nullable: false, fixedLength: true, timestamp: true, storeType: "rowversion"),
                    })
                .PrimaryKey(t => new { t.WeekNumber, t.Type, t.SubjectID,t.StudentID })
                .ForeignKey("dbo.Students", t => t.StudentID, cascadeDelete: true)
                .ForeignKey("dbo.Subjects", t => t.SubjectID, cascadeDelete: true)
                .ForeignKey("dbo.Teachers", t => t.TeacherID, cascadeDelete: true)
                .Index(t => t.StudentID)
                .Index(t => t.TeacherID)
                .Index(t => t.SubjectID);
            
            CreateTable(
                "dbo.Students",
                c => new
                    {
                        StudentID = c.Long(nullable: false, identity: true),
                        FirstName = c.String(),
                        LastName = c.String(),
                        GroupID = c.Long(nullable: false),
                        SubGroup = c.Int(nullable: false),
                        Year = c.Int(nullable: false),
                        Email = c.String(),
                        TimeStamp = c.Binary(nullable: false, fixedLength: true, timestamp: true, storeType: "rowversion"),
                    })
                .PrimaryKey(t => t.StudentID);
            
            CreateTable(
                "dbo.Subjects",
                c => new
                    {
                        SubjectID = c.Long(nullable: false, identity: true),
                        Title = c.String(),
                        TimeStamp = c.Binary(nullable: false, fixedLength: true, timestamp: true, storeType: "rowversion"),
                    })
                .PrimaryKey(t => t.SubjectID);
            
            CreateTable(
                "dbo.TeacherSubjects",
                c => new
                    {
                        GroupID = c.Long(nullable: false),
                        SubGroup = c.Int(nullable: false),
                        SubjectID = c.Long(nullable: false),
                        TeacherID = c.Long(nullable: false),
                        TimeStamp = c.Binary(nullable: false, fixedLength: true, timestamp: true, storeType: "rowversion"),
                    })
                .PrimaryKey(t => new { t.GroupID, t.SubGroup, t.SubjectID, t.TeacherID })
                .ForeignKey("dbo.Subjects", t => t.SubjectID, cascadeDelete: true)
                .ForeignKey("dbo.Teachers", t => t.TeacherID, cascadeDelete: true)
                .Index(t => t.SubjectID)
                .Index(t => t.TeacherID);
            
            CreateTable(
                "dbo.Teachers",
                c => new
                    {
                        TeacherID = c.Long(nullable: false, identity: true),
                        FirstName = c.String(),
                        LastName = c.String(),
                        Post = c.String(),
                        Email = c.String(),
                        TimeStamp = c.Binary(nullable: false, fixedLength: true, timestamp: true, storeType: "rowversion"),
                    })
                .PrimaryKey(t => t.TeacherID);
            
        }
        
        public override void Down()
        {
            DropForeignKey("dbo.TeacherSubjects", "TeacherID", "dbo.Teachers");
            DropForeignKey("dbo.Attendances", "TeacherID", "dbo.Teachers");
            DropForeignKey("dbo.TeacherSubjects", "SubjectID", "dbo.Subjects");
            DropForeignKey("dbo.Attendances", "SubjectID", "dbo.Subjects");
            DropForeignKey("dbo.Attendances", "StudentID", "dbo.Students");
            DropIndex("dbo.TeacherSubjects", new[] { "TeacherID" });
            DropIndex("dbo.TeacherSubjects", new[] { "SubjectID" });
            DropIndex("dbo.Attendances", new[] { "SubjectID" });
            DropIndex("dbo.Attendances", new[] { "TeacherID" });
            DropIndex("dbo.Attendances", new[] { "StudentID" });
            DropTable("dbo.Teachers");
            DropTable("dbo.TeacherSubjects");
            DropTable("dbo.Subjects");
            DropTable("dbo.Students");
            DropTable("dbo.Attendances");
        }
    }
}
