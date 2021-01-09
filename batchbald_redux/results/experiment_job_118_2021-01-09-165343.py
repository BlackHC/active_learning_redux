store = {}
store['timestamp']=1610211223
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py', '--id', '118']
store['commit']='5c070a811f5881af5b70b2a8785545ec5a64bad4'
store['github_url']='5c070a811f5881af5b70b2a8785545ec5a64bad4'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py'
store['job_id']=118
store['worker_id']=118
store['num_workers']=170
store['config']={'seed': 2120, 'acquisition_size': 50, 'max_training_set': 300, 'num_pool_samples': 20, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 10, 'validation_set_size': 4096, 'initial_set_size': 20, 'samples_per_epoch': 5056, 'repeated_mnist_repetitions': 2, 'add_dataset_noise': True, 'acquisition_function': 'AcquisitionFunction.thompsonbald', 'save_bald_scores': False, 'temperature': 0.0}
store['log']={}
store['initial_training_set_indices']=[38043, 40091, 17418, 2094, 39879, 3133, 5011, 40683, 54379, 24287, 9849, 59305, 39508, 39356, 8758, 52579, 13655, 7636, 21562, 41329]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 3.0490263998508453})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 3.3629338927567005})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.582763671875, 'crossentropy': 3.8230034299194813})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.58349609375, 'crossentropy': 3.7439288794994354})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evalution_metrics']={'accuracy': 0.5787, 'crossentropy': 3.091159036254883}
store['exception']='Traceback (most recent call last):\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py", line 656, in <module>\n    config.run(store=store)\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py", line 447, in run\n    candidate_batch = self.get_thompson_bald_candidate_batch(model, pool_loader)\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py", line 159, in get_thompson_bald_candidate_batch\n    candidate_batch = get_thompson_bald_batch(\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/batchbald.py", line 315, in get_thompson_bald_batch\n    assert K >= batch_size\nAssertionError\n'
