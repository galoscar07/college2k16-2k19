package View.GUI;

import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;

import Controller.Ctrl;
import Model.Expressions.ArithExp;
import Model.PrgState;
import Model.Statements.*;
import Model.Statements.HeapOperations.NewStmt;
import Model.Statements.HeapOperations.wH;
import Model.Statements.Loops.While;
import Model.Utils.*;
import Model.Expressions.ConstExp;
import Model.Expressions.rH;
import Model.Expressions.VarExp;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.ListView;
import javafx.stage.Stage;
import javafx.util.Callback;
import Repo.Repository;

import static javafx.collections.FXCollections.observableArrayList;

public class PrgListController implements Initializable {
    private static Repository myFirstRepository, myThirdRepository, myFourthRepository, myLastRepository;
    private static Ctrl myFirstController, myThirdController, myFourthController, myLastController;
    @FXML
	ListView<Ctrl> myPrgList;
	@FXML
	Button runButton;

	private void InitializePrgStates() {
        try {
            myFirstRepository = new Repository("f1.txt");
        } catch (IOException e) {
            e.printStackTrace();
        }
        myFirstController = new Ctrl(myFirstRepository);

        try {
            myThirdRepository = new Repository("f2.txt");
        } catch (IOException e) {
            e.printStackTrace();
        }
        myThirdController = new Ctrl(myThirdRepository);
        try {
            myFourthRepository = new Repository("f3.txt");
        } catch (IOException e) {
            e.printStackTrace();
        }
        myFourthController = new Ctrl(myFourthRepository);
        try {
            myLastRepository = new Repository("f4.txt");
        } catch (IOException e) {
            e.printStackTrace();
        }
        myLastController = new Ctrl(myLastRepository);
        IStmt firstProgram = new IfStmt(new ConstExp(10), new CompStmt(new CompStmt(new AssignStmt("v", new ConstExp(5)), new AssignStmt("m", new ConstExp(6))), new PrintStmt(new ArithExp('/', new VarExp("v"), new ConstExp(3)))), new PrintStmt(new ConstExp(100)));
        IStmt thirdProgram = new CompStmt(new AssignStmt("v", new ConstExp(10)), new CompStmt(new NewStmt("v", new ConstExp(20)), new CompStmt(new NewStmt("a", new ConstExp(22)), new CompStmt(new wH("a", new ConstExp(30)), new CompStmt(new PrintStmt(new VarExp("a")), new CompStmt(new PrintStmt(new rH("a")), new AssignStmt("a", new ConstExp(0))))))));
        IStmt fourthProgram = new CompStmt(new AssignStmt("v", new ConstExp(6)), new While(new ArithExp('-', new VarExp("v"), new ConstExp(4)), new CompStmt(new PrintStmt(new VarExp("v")), new AssignStmt("v", new ArithExp('-', new VarExp("v"), new ConstExp(1))))));
        IStmt lastProgram = new CompStmt(new AssignStmt("v", new ConstExp(10)), new CompStmt(new NewStmt("a", new ConstExp(22)), new CompStmt(new ForkStatement(new CompStmt(new wH("a", new ConstExp(30)), new CompStmt(new AssignStmt("v", new ConstExp(32)), new CompStmt(new PrintStmt(new VarExp("v")), new PrintStmt(new rH("a")))))), new CompStmt(new PrintStmt(new VarExp("v")), new PrintStmt(new rH("a"))))));
        MyIStack<IStmt> exeStack1 = new MyStack<IStmt>();
        MyIDictionary<String, Integer> symTable1 = new MyDictionary<String, Integer>();
        MyIList<Integer> out1 = new MyList<Integer>();
        ILatch la=new Latch();
        IFileTable< Tuple> fileTable1 = new FileTable<>();
        ILockTable l=new LockTable();
        MyIHeap<Integer> heap1 = new MyHeap<>();
        PrgState myPrgState1 = new PrgState(exeStack1, symTable1, out1, firstProgram, fileTable1, heap1,l,la,1);
        myFirstController.addProgram(myPrgState1);
        MyIStack<IStmt> exeStack3 = new MyStack<IStmt>();
        MyIDictionary<String, Integer> symTable3 = new MyDictionary<String, Integer>();
        MyIList<Integer> out3 = new MyList<Integer>();
        IFileTable< Tuple> fileTable3 = new FileTable<>();
        MyIHeap<Integer> heap3 = new MyHeap<>();
        PrgState myPrgState3 = new PrgState(exeStack3, symTable3, out3, thirdProgram, fileTable3, heap3,l,la,2 );
        myThirdController.addProgram(myPrgState3);
        MyIStack<IStmt> exeStack4 = new MyStack<IStmt>();
        MyIDictionary<String, Integer> symTable4 = new MyDictionary<String, Integer>();
        MyIList<Integer> out4 = new MyList<Integer>();
        IFileTable< Tuple> fileTable4 = new FileTable<>();
        MyIHeap<Integer> heap4 = new MyHeap<>();
        PrgState myPrgState4 = new PrgState(exeStack4, symTable4, out4, fourthProgram,fileTable4, heap4,l,la,3);
        myFourthController.addProgram(myPrgState4);
        MyIStack<IStmt> exeStack5 = new MyStack<IStmt>();
        MyIDictionary<String, Integer> symTable5= new MyDictionary<String, Integer>();
        MyIList<Integer> out5 = new MyList<Integer>();
        IFileTable< Tuple> fileTable5 = new FileTable<>();
        MyIHeap<Integer> heap5 = new MyHeap<>();
        PrgState myLastPrgState = new PrgState(exeStack5, symTable5, out5, lastProgram, fileTable5, heap5,l,la,4);
        myLastController.addProgram(myLastPrgState);

	}
	@Override
	public void initialize(URL location, ResourceBundle resources) {
		InitializePrgStates();
        ObservableList<Ctrl> myData = FXCollections.observableArrayList();
        myData.add(myFirstController);
        myData.add(myThirdController);
        myData.add(myFourthController);
        myData.add(myLastController);
		myPrgList.setItems(myData);
		myPrgList.getSelectionModel().selectFirst();
		runButton.setOnAction(new EventHandler<ActionEvent>() {
			@Override
			public void handle (ActionEvent e) {
				Stage programStage = new Stage();
				Parent programRoot;
				Callback<Class<?>, Object> controllerFactory = type -> {
				    if (type == PrgRunController.class) {
				        return new PrgRunController(myPrgList.getSelectionModel().getSelectedItem());
				    } else {
				        try {
				            return type.newInstance() ; 
				        } catch (Exception exc) {
				            System.err.println("Could not create Ctrl for "+type.getName());
				            throw new RuntimeException(exc);
				        }
				    }
				};
				try {
					FXMLLoader fxmlLoader = new FXMLLoader(getClass().getResource("ProgramLayout.fxml"));
					fxmlLoader.setControllerFactory(controllerFactory);
					programRoot = fxmlLoader.load();
					Scene programScene = new Scene(programRoot);
					programStage.setTitle("Toy Language - Program running");
					programStage.setScene(programScene);
					programStage.show();
				} catch (IOException e1) {
					e1.printStackTrace();
				}
			}
		});
	}

}
