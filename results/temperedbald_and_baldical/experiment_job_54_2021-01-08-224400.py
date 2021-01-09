store = {}
store['timestamp']=1610145840
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py', '--id', '54']
store['commit']='466d7e4a4eedcd2b9dd80c52983a524624d138a9'
store['github_url']='466d7e4a4eedcd2b9dd80c52983a524624d138a9'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py'
store['job_id']=54
store['worker_id']=54
store['num_workers']=100
store['config']={'seed': 395, 'acquisition_size': 5, 'max_training_set': 300, 'num_pool_samples': 20, 'num_eval_samples': 4, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 10, 'validation_set_size': 4096, 'initial_set_size': 20, 'samples_per_epoch': 24576, 'repeated_mnist_repetitions': 2, 'add_dataset_noise': True, 'acquisition_function': 'AcquisitionFunction.temperedbaldical', 'save_bald_scores': False, 'temperature': 13}
store['log']={}
store['initial_training_set_indices']=[38043, 40091, 17418, 2094, 39879, 3133, 5011, 40683, 54379, 24287, 9849, 59305, 39508, 39356, 8758, 52579, 13655, 7636, 21562, 41329]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.514892578125, 'crossentropy': 8.414080627262592})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.51611328125, 'crossentropy': 9.404956616461277})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.51220703125, 'crossentropy': 7.5415142104029655})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.531982421875, 'crossentropy': 9.424723230302334})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.535400390625, 'crossentropy': 8.839363545179367})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.53759765625, 'crossentropy': 8.64602979272604})
store['active_learning_steps'][0]['training']['best_epoch']=3
store['active_learning_steps'][0]['evalution_metrics']={'accuracy': 0.5352, 'crossentropy': 7.542985175323486}
store['active_learning_steps'][0]['pool_training']={}
store['active_learning_steps'][0]['pool_training']['epochs']=[]
store['active_learning_steps'][0]['pool_training']['epochs'].append({'accuracy': 0.53076171875, 'crossentropy': 7.137673515826464})
store['active_learning_steps'][0]['pool_training']['epochs'].append({'accuracy': 0.537109375, 'crossentropy': 6.27615125849843})
store['active_learning_steps'][0]['pool_training']['epochs'].append({'accuracy': 0.533447265625, 'crossentropy': 6.685825414955616})
store['active_learning_steps'][0]['pool_training']['best_epoch']=2
store['exception']='Traceback (most recent call last):\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py", line 545, in <module>\n    config.run(store=store)\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py", line 385, in run\n    candidate_batch = self.get_bald_ical_candidate_batch(\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py", line 218, in get_bald_ical_candidate_batch\n    candidate_batch = get_scorers(scores_N, batch_size=self.acquisition_size)\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py", line 389, in <lambda>\n    get_scorers=lambda scores_N, batch_size: get_sampled_tempered_scorers(\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/batchbald.py", line 418, in get_sampled_tempered_scorers\n    candidate_indices = np.random.choice(N, size=batch_size, replace=False, p=p)\n  File "mtrand.pyx", line 930, in numpy.random.mtrand.RandomState.choice\nValueError: probabilities are not non-negative\n'
