using sharplab.Model.Statements;
using System;
using System.Collections.Generic;
using System.Text;

namespace sharplab.Model.Utils
{
    class PrgState
    {
        private IMyStack<IStmt> exeStack;
        private IMyDictionary<string, int> symTable;
        private IMyList<int> o;
        private IStmt originalProgram;
        private IFileTable<Tuple> fileTbl;
       

        public PrgState(IMyStack<IStmt> exeStack, IMyDictionary<string, int> symTable, IMyList<int> o, IStmt prg, IFileTable<Tuple> fileT)
        {
            this.exeStack = exeStack;
            this.symTable = symTable;
            this.o = o;
            this.originalProgram = prg;
            this.fileTbl = fileT;
            exeStack.Push(prg);
        }

        public IMyStack<IStmt> GetStk()
        {
            return exeStack;
        }

        public void SetStk(MyStack<IStmt> stk)
        {
            this.exeStack = stk;
        }

        public IMyDictionary<string, int> GetSymTable()
        {
            return symTable;
        }

        public void SetDict(IMyDictionary<string, int> dict)
        {
            this.symTable = dict;
        }

        public IMyList<int> Geto()
        {
            return o;
        }

        public IFileTable<Tuple> GetFT() { return fileTbl; }

        public void SetList(IMyList<int> list)
        {
            this.o = list;
        }

        public IStmt GetOriginalProgram() { return originalProgram; }

       
    }
}
