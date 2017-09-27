/**
 * @author AsuraDong
 * @time 2017/9/19 21:09
 */
package calculator;
import java.util.*;

class Level {
	protected HashMap<String,Integer> level = new HashMap<String,Integer>();
	Level (){
		level.put("+", 1);
		level.put("-", 1);
		level.put("*", 3);
		level.put("/", 3);
		level.put("cos",5);
		level.put("sin",5);
		level.put("(", 7);
		level.put(")", 7);
	}
	public void addLevel(String op,int lev) {
		level.put(op, lev);
	}
	public HashMap<String,Integer> getLevel() {
		return level;
	}
}

public class Transform extends Level{
	private Stack<String> op_stack  = new Stack<String>(); // operator_stack
	private Stack<String> res_stack = new Stack<String>(); // result_stack
	public String calc="";
	Transform (String calc){	
		this.calc = calc.replaceAll(" ","");
		if(this.calc.substring(0, 1).equals("-")) 
			this.calc = "0" + this.calc;
	}
	public void transCalc() {
		String number = "0123456789";
		String operator = "+/-*()";
		String letter = "abcdefghijklmnopqrstuvwxyz";
		for(int i=0;i<calc.length();++i) {
			String op = calc.substring(i, i+1); //op当前符号或数字
			if(number.indexOf(op)!=-1){ // 数字直接推入结果栈
				String multi_num = op;				
				while(i+1<calc.length() &&  ( calc.substring(i+1,i+2).equals(".") ||  number.indexOf(calc.substring(i+1, i+2))!=-1 )) { //如果下一个字符是数字的话
					i = i+1;
					op = calc.substring(i, i+1); //得到下一个字符
					multi_num += op;
				}
				res_stack.push(multi_num);
			} 
			else if (operator.indexOf(op)!=-1) { // 如果是符号
				if(!op_stack.isEmpty())  {
					String pre_op = op_stack.peek(); // 符号栈中的上一个操作符
					while(level.get(pre_op)>=level.get(op) && !pre_op.equals("(")) { // 注意要判断左括号的内容
						res_stack.push(op_stack.pop()); // 将符号栈中的上一个操作符弹出后推入结果栈
						if (!op_stack.isEmpty())
							pre_op = op_stack.peek();
						else break;
					}
				}
				if (op.equals(")")) {
					String pre_op = op_stack.peek(); 
					while(!pre_op.equals("(")) {
						res_stack.push(op_stack.pop());
						pre_op = op_stack.peek(); 
					}
					op_stack.pop(); // 最后一定是左括号，弹出
				}
				else 
					op_stack.push(op);
			} 
			else if (letter.indexOf(op)!=-1){ // 处理cos，sin，tan，sqrt等特殊运算符
				String multi_num = op; 
				while(i+1<calc.length() && letter.indexOf(calc.substring(i+1,i+2))!=-1) {
					i = i+1;
					op = calc.substring(i,i+1);
					multi_num+=op;
				}
				op_stack.push(multi_num);
			}
		}
		while(!op_stack.isEmpty()) {
			res_stack.push(op_stack.pop());
		}
	}
	public double getResult() {
		String operator = "+/-*()";
		String other_operator = "cos sin";
		Vector<String> res_vec = new Vector<String>();
		while(!res_stack.isEmpty()) {
			res_vec.add(0,res_stack.pop());
		}
		for(int i=0;i<res_vec.size() && res_vec.size()>1 ;++i) {
			if(operator.indexOf(res_vec.get(i))!=-1) { // 如果检索到符号
				double  last_num = Double.parseDouble(res_vec.get(i-1));
				double last_last_num = Double.parseDouble(res_vec.get(i-2));
				double temp = operateElem(last_last_num,last_num,res_vec.get(i));
				res_vec.remove(i);
				res_vec.remove(i-1);
				res_vec.remove(i-2);
				res_vec.add(i-2,Double.toString(temp));
				i = i-2;
			}
			else if (other_operator.indexOf(res_vec.get(i))!=-1) {
				double last_num = Double.parseDouble(res_vec.get(i-1));
				double temp = moreOperateElem(last_num,res_vec.get(i));
				res_vec.remove(i);
				res_vec.remove(i-1);
				res_vec.add(i-1,Double.toString(temp));
				i = i-1;
			}
		}
		return Double.parseDouble(res_vec.get(0)); // 最后的结果栈一定只有一个值
	}
	public void showResStack() {
		System.out.println(res_stack);
	}
	private double moreOperateElem(double last_num,String tag) {
		switch(tag) {
		case "cos":
			return Math.cos(last_num);
		case "sin":
			return Math.sin(last_num);
		default:
			return 0;
		}
	}
	private double operateElem(double a,double b,String tag) { // 计算符号
		switch(tag) {
		case "+":
			return a+b;
		case "-":
			return a-b;
		case "/":
			return a/b;
		case "*":
			return a*b;
		default:
			return 0;
		}
	}
	public static void main(String[]args) {
		Scanner scan2 = new Scanner(System.in);
		Scanner scan = new Scanner(System.in);
		int n = scan2.nextInt();
		
		while(true) {
			if(n==0)
				break;
//			System.out.println("请输入计算表达式：");
			String calc = scan.nextLine();
//			if (calc.equals("q") || calc.equals("quit"))
//				break;
			Transform mytrans  = new Transform(calc.substring(0, calc.length()-1));
			mytrans.transCalc();
//			System.out.print("后缀表达式：");
//			mytrans.showResStack();
			double res = mytrans.getResult();
			System.out.printf("%.4f\n", res);
			n--;
		}
	}
}