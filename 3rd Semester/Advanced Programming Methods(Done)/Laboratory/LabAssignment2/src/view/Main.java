package view;

import controller.Controller;
import models.ArithmeticExpression;
import models.AssignStatement;
import models.CompoundStatement;
import models.ConstExpression;
import models.Dictionary;
import models.ExecStack;
import models.IDictionary;
import models.IExecStack;
import models.IList;
import models.MyList;
import models.PrintStatement;
import models.ProgramState;
import models.Statement;
import models.VariableExpression;
import repository.IProgramStateRepository;
import repository.ProgramStateRepository;

public class Main {
	public static void main(String[] a) {
		Statement st = new CompoundStatement(new AssignStatement("v",new ConstExpression(2)),new PrintStatement(new VariableExpression("v")));
		Statement as = new AssignStatement("num",new ArithmeticExpression('+',new VariableExpression("v"),new ConstExpression(3)));
		Statement s = new CompoundStatement(new CompoundStatement(st,as),new PrintStatement(new VariableExpression("num")));
		IExecStack<Statement> es = new ExecStack<>();
		es.push(s);
		IDictionary<String,Integer> dict = new Dictionary<>();
		IList<Integer> list = new MyList<>();
		ProgramState ps = new ProgramState(es,dict,list,st);
		IProgramStateRepository rep = new ProgramStateRepository();
		rep.addProgramState(ps);
		Controller ctrl = new Controller(rep);
		ctrl.executeAll();
	}
}
