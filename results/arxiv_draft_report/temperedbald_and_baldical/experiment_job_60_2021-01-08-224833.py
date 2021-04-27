store = {}
store['timestamp']=1610146113
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py', '--id', '60']
store['commit']='466d7e4a4eedcd2b9dd80c52983a524624d138a9'
store['github_url']='466d7e4a4eedcd2b9dd80c52983a524624d138a9'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py'
store['job_id']=60
store['worker_id']=60
store['num_workers']=100
store['config']={'seed': 401, 'acquisition_size': 20, 'max_training_set': 300, 'num_pool_samples': 20, 'num_eval_samples': 4, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 10, 'validation_set_size': 4096, 'initial_set_size': 20, 'samples_per_epoch': 24576, 'repeated_mnist_repetitions': 2, 'add_dataset_noise': True, 'acquisition_function': 'AcquisitionFunction.temperedbaldical', 'save_bald_scores': False, 'temperature': 13}
store['log']={}
store['initial_training_set_indices']=[38043, 40091, 17418, 2094, 39879, 3133, 5011, 40683, 54379, 24287, 9849, 59305, 39508, 39356, 8758, 52579, 13655, 7636, 21562, 41329]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.55517578125, 'crossentropy': 7.347490757703781})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.563232421875, 'crossentropy': 7.157526083290577})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.546142578125, 'crossentropy': 6.6187200248241425})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.549072265625, 'crossentropy': 6.076782088726759})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.542236328125, 'crossentropy': 6.501858487725258})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.56591796875, 'crossentropy': 6.067149039357901})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.53857421875, 'crossentropy': 5.309852436184883})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5537109375, 'crossentropy': 5.7800818383693695})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.567138671875, 'crossentropy': 5.3224337585270405})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.557861328125, 'crossentropy': 7.212145894765854})
store['active_learning_steps'][0]['training']['best_epoch']=7
store['active_learning_steps'][0]['evalution_metrics']={'accuracy': 0.537, 'crossentropy': 5.531084936523437}
store['active_learning_steps'][0]['pool_training']={}
store['active_learning_steps'][0]['pool_training']['epochs']=[]
store['active_learning_steps'][0]['pool_training']['epochs'].append({'accuracy': 0.5537109375, 'crossentropy': 5.34130997210741})
store['active_learning_steps'][0]['pool_training']['epochs'].append({'accuracy': 0.541748046875, 'crossentropy': 5.344703417271376})
store['active_learning_steps'][0]['pool_training']['epochs'].append({'accuracy': 0.543701171875, 'crossentropy': 5.108334187418222})
store['active_learning_steps'][0]['pool_training']['epochs'].append({'accuracy': 0.544677734375, 'crossentropy': 5.25743068754673})
store['active_learning_steps'][0]['pool_training']['epochs'].append({'accuracy': 0.550537109375, 'crossentropy': 4.8153047151863575})
store['active_learning_steps'][0]['pool_training']['epochs'].append({'accuracy': 0.541015625, 'crossentropy': 5.013710863888264})
store['active_learning_steps'][0]['pool_training']['epochs'].append({'accuracy': 0.5478515625, 'crossentropy': 5.185400940477848})
store['active_learning_steps'][0]['pool_training']['best_epoch']=5
store['exception']='Traceback (most recent call last):\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py", line 545, in <module>\n    config.run(store=store)\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py", line 385, in run\n    candidate_batch = self.get_bald_ical_candidate_batch(\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py", line 218, in get_bald_ical_candidate_batch\n    candidate_batch = get_scorers(scores_N, batch_size=self.acquisition_size)\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py", line 389, in <lambda>\n    get_scorers=lambda scores_N, batch_size: get_sampled_tempered_scorers(\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/batchbald.py", line 418, in get_sampled_tempered_scorers\n    candidate_indices = np.random.choice(N, size=batch_size, replace=False, p=p)\n  File "mtrand.pyx", line 930, in numpy.random.mtrand.RandomState.choice\nValueError: probabilities are not non-negative\n'
