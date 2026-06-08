from dataset_profiler import DatasetProfiler
if __name__=="__main__":
    profiler=DatasetProfiler("../../datasets/raw/finance/loan_prediction.csv")
    result=profiler.profile()
    print(result)
    