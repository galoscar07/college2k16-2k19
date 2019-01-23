package models;

public class ProgramState {
	private IExecStack<Statement> execStack;
	private IDictionary<String,Integer> symbolT;
	private IList<Integer> messages;
	private Statement rootP;
	
	public ProgramState(IExecStack<Statement> es,IDictionary<String,Integer> st, IList<Integer> m,Statement rp) {
		execStack = es;
		symbolT = st;
		messages = m;
		rootP = rp;
	}
	
	@Override
	public String toString() {
		StringBuffer sb = new StringBuffer();
		sb.append(">>>>>\n");
		if(!execStack.toString().isEmpty()) {
			sb.append("Execution Stack: \n" + execStack);
		}
		if(!symbolT.toString().isEmpty()) {
			sb.append("Symbol Table: \n" + symbolT);
		}
		if(!messages.toString().isEmpty()) {
			sb.append("Screen: \n" + messages);
		}
		//if(!rootP.toString().isEmpty()) {
		//	sb.append("Root Statement: " + rootP);
		//}
		sb.append(">>>>>");
		return sb.toString();
	}
	
	public IDictionary<String,Integer> getSymbolTable(){
		return symbolT;
	}
	
	public IExecStack<Statement> getExecStack(){
		return execStack;
	}
	
	public IList<Integer> getList(){
		return messages;
	}
}
