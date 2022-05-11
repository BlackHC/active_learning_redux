store = {}
store['timestamp']=1651879323
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/poc_online_bayesian_inference.py', '--id=0']
store['commit']='6f7d411c4772d2f8e6f1ffcaf7a8fff819a217f7'
store['github_url']='6f7d411c4772d2f8e6f1ffcaf7a8fff819a217f7'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/poc_online_bayesian_inference.py'
store['job_id']=0
store['worker_id']=0
store['num_workers']=8
store['config']={'seed': 1337, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 20, 'max_training_epochs': 120, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'min_samples_per_epoch': 1024, 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'max_obi_steps': 10, 'num_samples_list': [10000], 'up_factor': 2, 'num_trials': 5, 'acquisition_size': 1, 'random_acquisition': True}
store['log']={}
store['exception']='Traceback (most recent call last):\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/poc_online_bayesian_inference.py", line 502, in <module>\n    config.run(store=store)\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/poc_online_bayesian_inference.py", line 364, in run\n    init_wandb(self)\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_logging.py", line 87, in init_wandb\n    wandb.init(\n  File "/scratch-ssd/andsch/tmp/conda_envs/job-61559/lib/python3.8/site-packages/wandb/sdk/wandb_init.py", line 999, in init\n    run = wi.init()\n  File "/scratch-ssd/andsch/tmp/conda_envs/job-61559/lib/python3.8/site-packages/wandb/sdk/wandb_init.py", line 653, in init\n    raise UsageError(error_message)\nwandb.errors.UsageError: Error communicating with wandb process\ntry: wandb.init(settings=wandb.Settings(start_method=\'fork\'))\nor:  wandb.init(settings=wandb.Settings(start_method=\'thread\'))\nFor more info see: https://docs.wandb.ai/library/init#init-start-error\n'
