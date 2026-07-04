
    namespace MyProgram {
        open Microsoft.Quantum.Intrinsic;
        open Microsoft.Quantum.Measurement;
        operation Main(): Unit{
            let n = 5;
            let a = [1, 1, 0, 1, 1];
            use qc = Qubit[n + 1];
            X(qc[n]);
            //first hadamard
            for i in 0..n{
                H(qc[i]); 
            }
            //oracle
            for i in 0..(n-1){
                if (a[i] == 1){
                    CNOT(qc[i], qc[n]);
                }
            }
            //second hadamard
            for i in 0..n{
                H(qc[i]); 
            }
            //result
            for i in 0..(n-1){
                if (M(qc[i]) == One){
                    Message("1");
                }else{Message("0");}
            }
        }
    }