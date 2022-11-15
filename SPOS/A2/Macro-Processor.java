import java.io.DataInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;

class MacroProcessor {
	
	private static HashMap<String,Integer> mnt = new HashMap<String,Integer>(); 
	private static ArrayList<String> mdt = new ArrayList<String>(),ala = new ArrayList<String>();
	private static String FileContent;
	private static Pass1 pass1 = new Pass1();
	private static Pass2 pass2 = new Pass2();

	public static void main(String[] args) throws IOException {
		
		System.out.println("\n\n******** Two Pass Macro-Processor **********\n\n");
		/*System.out.println("Enter Name of File containing assembler program\n");
		String FileName = scan.nextLine();*/
		FileContent = getContentFrom("InputFile.txt");
		//System.out.println(FileContent +"Contents of MNT are : \n\n");
		pass1.start();
		
		System.out.println("Ouput of Pass-1 Macro Processor -: \n\n");
		System.out.println("Contents of MNT are : \n\n");
		System.out.println(mnt);
		
		System.out.println("\n\nContents of MDT are : \n\n");
		//System.out.println(mdt);
		for(int i=0; i<mdt.size(); i++)
		{
			System.out.println(mdt.get(i));
		}	
		System.out.println("\n\nContents of ALA are : \n");
		System.out.println(ala);
		
		pass2.start();

	}

	private static String getContentFrom(String fileName) throws IOException {
		
		String content;
		File file = new File(fileName);
		FileInputStream fis = new FileInputStream(file);
		DataInputStream dis = new DataInputStream(fis);

		int f_count = fis.available();

		byte[] b = new byte[f_count];
		dis.readFully(b);

		content = new String(b);
		
		dis.close();
		return content;
	}

	public static String getFileContent() {
		return MacroProcessor.FileContent;
	}
	
	public static Integer getIndexFromMnt(String name) {
		
		if(mnt.containsKey(name))
			return mnt.get(name);
		return -1;
	}

	public static Boolean mntContains(String name) {
		
		if(mnt.containsKey(name))
			return true;
		
		return false;
		
	}
	
	public static void updateMnt(String name, int mdtp) {
		mnt.put(name, mdtp);
	}
	
	public static Boolean inMnt(String name) {
		
			if(mnt.get(name) == null) {
				return false;
			}
		
		return true;
	}

	public static String getLineFromMdt(int index) {
		return mdt.get(index);
	}

	public static void updateMdt(String line) {
		mdt.add(line);
	}

	public static String getLineFromAla(int index) {
		return ala.get(index);
	}

	public static void updateAla(String arg) {
		ala.add(arg);
	}
	
	public static String getArgumentAtIndex(int index) {
		return ala.get(index);
	}
	
	public static int getAlaSize() {
		return ala.size();
	}
	
	public static void initAla() {
		ala = new ArrayList<String>();
	}

	public void prepareALA(String[] lineContent2) {
		
		if(lineContent2[1].matches(".+,.+")) {
			String[] commaSepr = lineContent2[1].split(",");
			for(int i=0; i<commaSepr.length; i++) {
				updateAla(commaSepr[i]);
			}
			return;
		}
		for(int i=1; i<lineContent2.length; i++) {
			updateAla(lineContent2[i]);
		}
		
	}

}


 class Pass2 extends MacroProcessor {
	
	private String newFileContent = "";
	private String finalFileContent = "";
	private int mdtp;
	
	public void start() {
		
		updateFileContent();
		String[] lineContent = newFileContent.split("\\r?\\n");
		
		for(String currentLine : lineContent) {
			
			String[] line = currentLine.split("\\s+");
			
			if(macroNameFoundAt(line)) {
				
				//System.out.println("macro name found " + line[0]);
			
				mdtp = getIndexFromMnt(line[0]);
				mdtp++;
				
				prepareALA(line);
				
				String mdtLine = getLineFromMdt(mdtp);
				while(!mdtLine.equals("MEND")) {
					
					String[] mdtspace = mdtLine.split("\\s+");
					
					finalFileContent = finalFileContent + mdtspace[0] + " ";
					for(int i=1; i<mdtspace.length; i++) {
						//System.out.println(mdtspace[i]);
						mdtspace[i] = getLineFromAla(Integer.parseInt(mdtspace[i]));
						finalFileContent = finalFileContent + mdtspace[i] + " ";
					}
					//mdtLine = mdtspace.toString();
					finalFileContent = finalFileContent + "\n";
					mdtLine = getLineFromMdt(++mdtp);
					
				}
				
				initAla();
				continue;
				
			}
			
			finalFileContent = finalFileContent + currentLine + "\n";
			
		}
		
		System.out.println("\n\nOutput of Pass-2 Macro Processor is  : \n\n"+finalFileContent);
		
	}

	private boolean macroNameFoundAt(String[] line) {
		
		String macroName = "";
		macroName = line[0];
		
		if(mntContains(macroName))
			return true;
		
		return false;
	}

	private void updateFileContent() {
		
		String[] temp = getFileContent().split("\\r?\\n");
		int i = 0;
		while(!temp[i].contains("START")) 
			i++;
		
		for(;i<temp.length;i++) {
			
			newFileContent = newFileContent + temp[i] + "\n";
			
		}
		
	}

	
}


class Pass1 extends MacroProcessor{
	
	private String[] fileContent,lineContent;
	private String currentLine;
	private int mdtp = 0;
	
	public void start() {
		
		int i=1;
		fileContent = getFileContent().split("\\r?\\n");
		currentLine = fileContent[0];
		
		while(!currentLine.equals("END")) {
			
			lineContent = currentLine.split("\\s+");
			
			if(lineContent[0].equals("MACRO")) {
				
				currentLine = fileContent[i++];
				lineContent = currentLine.split("\\s+");
				if(inMnt(lineContent[0])) {
					System.out.println(lineContent[0] + " already exists !!!!, Skipping this MACRO");
					continue;
				}
				updateMnt(lineContent[0],mdtp);
				prepareALA(lineContent);
				updateMdt(this.currentLine);
				mdtp++;
				currentLine = fileContent[i++];
				
				while(!currentLine.equals("MEND")) {
					
					String substitutedLine = substitute_index_notation(currentLine);
					updateMdt(substitutedLine);
					mdtp++;
					currentLine = fileContent[i++];
					
				}
				
				updateMdt("MEND");
				mdtp++;
				initAla();
				continue;
			}
			currentLine = fileContent[i++];
			
		}
		
	}

	private String substitute_index_notation(String currentLine2) {
		
		lineContent = currentLine.split("\\s+");
		String subsLine = "";
		Boolean isFound = false;
		int alaSize = getAlaSize();
		for(String currentWord : lineContent) {
			
			if(currentWord.matches(".+,.+")) {
				
				String[] commaSepr = currentWord.split(",");
				for(String comma : commaSepr) {
					for(int i=0; i<alaSize; i++) {
						if(comma.equals(getArgumentAtIndex(i))) {
							subsLine = subsLine +  i + " ";
							isFound = true;
							break;
						}
					}
				}
				
				
			}else {
				for(int i=0; i<alaSize; i++) {
					if(currentWord.equals(getArgumentAtIndex(i))) {
						subsLine = subsLine + i + " ";
						isFound = true;
						break;
					}
				}
				if(!isFound)
				subsLine = subsLine + currentWord + " ";
			}
			
		}
		
		return subsLine;
	}

}
