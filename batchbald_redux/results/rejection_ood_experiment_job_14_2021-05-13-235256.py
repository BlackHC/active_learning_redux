store = {}
store['timestamp']=1620946376
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=14']
store['commit']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['github_url']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=14
store['worker_id']=14
store['num_workers']=20
store['config']={'seed': 1255, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 100, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['exception']='Traceback (most recent call last):\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py", line 318, in <module>\n    config.run(store=store)\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py", line 173, in run\n    data = self.load_experiment_data()\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py", line 88, in load_experiment_data\n    FastMNIST("data", train=True, download=True, device=self.device), "FastMNIST (train)"\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/fast_mnist.py", line 28, in __init__\n    self.data, self.targets = self.data.to(device), self.targets.to(device)\n  File "/scratch-ssd/andsch/tmp/conda_envs/job-5965/lib/python3.8/site-packages/torch/cuda/__init__.py", line 170, in _lazy_init\n    torch._C._cuda_init()\nRuntimeError: CUDA driver initialization failed, you might not have a CUDA gpu.\n'
