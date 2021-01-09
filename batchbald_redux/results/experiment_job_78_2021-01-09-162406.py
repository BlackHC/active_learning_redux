store = {}
store['timestamp']=1610209446
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py', '--id', '78']
store['commit']='5c070a811f5881af5b70b2a8785545ec5a64bad4'
store['github_url']='5c070a811f5881af5b70b2a8785545ec5a64bad4'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py'
store['job_id']=78
store['worker_id']=78
store['num_workers']=170
store['config']={'seed': 2078, 'acquisition_size': 50, 'max_training_set': 300, 'num_pool_samples': 20, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 10, 'validation_set_size': 4096, 'initial_set_size': 20, 'samples_per_epoch': 5056, 'repeated_mnist_repetitions': 2, 'add_dataset_noise': True, 'acquisition_function': 'AcquisitionFunction.thompsonbald', 'save_bald_scores': False, 'temperature': 0.0}
store['log']={}
store['initial_training_set_indices']=[38043, 40091, 17418, 2094, 39879, 3133, 5011, 40683, 54379, 24287, 9849, 59305, 39508, 39356, 8758, 52579, 13655, 7636, 21562, 41329]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.56103515625, 'crossentropy': 3.0027029532939196})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.556396484375, 'crossentropy': 3.3557595144957304})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.576416015625, 'crossentropy': 3.4068004600703716})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.558349609375, 'crossentropy': 3.862298935651779})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evalution_metrics']={'accuracy': 0.5603, 'crossentropy': 2.8665350719451905}
store['exception']='Traceback (most recent call last):\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py", line 656, in <module>\n    config.run(store=store)\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py", line 447, in run\n    candidate_batch = self.get_thompson_bald_candidate_batch(model, pool_loader)\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py", line 159, in get_thompson_bald_candidate_batch\n    candidate_batch = get_thompson_bald_batch(\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/batchbald.py", line 315, in get_thompson_bald_batch\n    assert K >= batch_size\nAssertionError\n'
