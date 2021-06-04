store = {}
store['timestamp']=1622790120
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py', '--id=47']
store['commit']='03f69f03c653152ecfa74b84289906c55ed08e71'
store['github_url']='03f69f03c653152ecfa74b84289906c55ed08e71'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py'
store['job_id']=47
store['worker_id']=47
store['num_workers']=60
store['config']={'seed': 839, 'acquisition_size': 5, 'max_training_set': 300, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 20, 'max_training_epochs': 120, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 2048, 'initial_set_size': 20, 'min_samples_per_epoch': 1024, 'repeated_mnist_repetitions': 2, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEIG', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['initial_training_set_indices']=[38043, 40091, 17418, 2094, 39879, 3133, 5011, 40683, 54379, 24287, 9849, 59305, 39508, 39356, 8758, 52579, 13655, 7636, 21562, 41329]
store['dataset_info']={'training': "'FastMNIST (Train)'x2", 'test': "'FastMNIST (Test)'"}
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5361328125, 'crossentropy': 1.948535442352295})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.7655141353607178})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.62451171875, 'crossentropy': 2.220689296722412})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.65087890625, 'crossentropy': 2.3577194213867188})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.64697265625, 'crossentropy': 2.562561273574829})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.64208984375, 'crossentropy': 2.5838770866394043})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.8024187088012695})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.8770365715026855})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.65087890625, 'crossentropy': 3.0496749877929688})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.1367549896240234})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.63525390625, 'crossentropy': 3.1415231227874756})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.63134765625, 'crossentropy': 3.189635992050171})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.63525390625, 'crossentropy': 3.115945816040039})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.1509480476379395})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.06217622756958})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.2658348083496094})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.5976510047912598})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.62939453125, 'crossentropy': 3.385439872741699})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.302244186401367})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.1945436000823975})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.352452278137207})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.62353515625, 'crossentropy': 3.3918204307556152})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.63037109375, 'crossentropy': 3.353006362915039})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.64013671875, 'crossentropy': 3.376668930053711})
store['active_learning_steps'][0]['training']['best_epoch']=4
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6489, 'crossentropy': 2.3682521484375}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.4091796875, 'crossentropy': 1.9895727634429932})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.61376953125, 'crossentropy': 1.5070686340332031})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.63916015625, 'crossentropy': 1.3714066743850708})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.2854751348495483})
store['active_learning_steps'][0]['eval_training']['best_epoch']=4
store['exception']='Traceback (most recent call last):\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py", line 264, in <module>\n    config.run(store=store)\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py", line 208, in run\n    candidate_batch = acquisition_function.compute_candidate_batch(\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/acquisition_functions.py", line 232, in compute_candidate_batch\n    return self.get_candidate_batch(log_probs_N_K_C, log_eval_probs_N_K_C, device)\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/acquisition_functions.py", line 313, in get_candidate_batch\n    num_samples=self.num_samples,\nAttributeError: \'BatchEIG\' object has no attribute \'num_samples\'\n'
