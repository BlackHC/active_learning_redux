store = {}
store['timestamp']=1622796638
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py', '--id=59']
store['commit']='03f69f03c653152ecfa74b84289906c55ed08e71'
store['github_url']='03f69f03c653152ecfa74b84289906c55ed08e71'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py'
store['job_id']=59
store['worker_id']=59
store['num_workers']=60
store['config']={'seed': 852, 'acquisition_size': 5, 'max_training_set': 300, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 20, 'max_training_epochs': 120, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 2048, 'initial_set_size': 20, 'min_samples_per_epoch': 1024, 'repeated_mnist_repetitions': 2, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEIG', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['initial_training_set_indices']=[38043, 40091, 17418, 2094, 39879, 3133, 5011, 40683, 54379, 24287, 9849, 59305, 39508, 39356, 8758, 52579, 13655, 7636, 21562, 41329]
store['dataset_info']={'training': "'FastMNIST (Train)'x2", 'test': "'FastMNIST (Test)'"}
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.55859375, 'crossentropy': 1.9342458248138428})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.63134765625, 'crossentropy': 1.7852282524108887})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 2.3969781398773193})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.3176708221435547})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.4519803524017334})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.7208151817321777})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.5361063480377197})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.9058687686920166})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.64111328125, 'crossentropy': 2.829089879989624})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.160836935043335})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.1188292503356934})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.437856435775757})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.211254119873047})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 3.4564590454101562})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.62158203125, 'crossentropy': 3.2633461952209473})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.2652997970581055})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.4081361293792725})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.5007760524749756})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.63232421875, 'crossentropy': 3.4086508750915527})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.628282308578491})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.6794350147247314})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.4512927532196045})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.57958984375, 'crossentropy': 4.093270778656006})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.63232421875, 'crossentropy': 3.1909990310668945})
store['active_learning_steps'][0]['training']['best_epoch']=4
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6588, 'crossentropy': 2.27779453125}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.361328125, 'crossentropy': 2.0205228328704834})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.544921875, 'crossentropy': 1.614786148071289})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.3909156322479248})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.63134765625, 'crossentropy': 1.3526971340179443})
store['active_learning_steps'][0]['eval_training']['best_epoch']=4
store['exception']='Traceback (most recent call last):\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py", line 264, in <module>\n    config.run(store=store)\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py", line 208, in run\n    candidate_batch = acquisition_function.compute_candidate_batch(\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/acquisition_functions.py", line 232, in compute_candidate_batch\n    return self.get_candidate_batch(log_probs_N_K_C, log_eval_probs_N_K_C, device)\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/acquisition_functions.py", line 313, in get_candidate_batch\n    num_samples=self.num_samples,\nAttributeError: \'BatchEIG\' object has no attribute \'num_samples\'\n'
