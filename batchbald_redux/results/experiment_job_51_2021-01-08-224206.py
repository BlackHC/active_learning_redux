store = {}
store['timestamp']=1610145726
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py', '--id', '51']
store['commit']='466d7e4a4eedcd2b9dd80c52983a524624d138a9'
store['github_url']='466d7e4a4eedcd2b9dd80c52983a524624d138a9'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py'
store['job_id']=51
store['worker_id']=51
store['num_workers']=100
store['config']={'seed': 391, 'acquisition_size': 50, 'max_training_set': 300, 'num_pool_samples': 20, 'num_eval_samples': 4, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 10, 'validation_set_size': 4096, 'initial_set_size': 20, 'samples_per_epoch': 24576, 'repeated_mnist_repetitions': 2, 'add_dataset_noise': True, 'acquisition_function': 'AcquisitionFunction.temperedbaldical', 'save_bald_scores': False, 'temperature': 13}
store['log']={}
store['initial_training_set_indices']=[38043, 40091, 17418, 2094, 39879, 3133, 5011, 40683, 54379, 24287, 9849, 59305, 39508, 39356, 8758, 52579, 13655, 7636, 21562, 41329]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.60888671875, 'crossentropy': 3.7828286923468113})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.622802734375, 'crossentropy': 3.7445452734827995})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.56982421875, 'crossentropy': 4.134159963577986})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.615478515625, 'crossentropy': 3.5855447724461555})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.603759765625, 'crossentropy': 4.412691067904234})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.626708984375, 'crossentropy': 3.824360378086567})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.61767578125, 'crossentropy': 3.4867744483053684})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.600830078125, 'crossentropy': 4.373604349792004})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.621826171875, 'crossentropy': 3.4255540277808905})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.5644177310168743})
store['active_learning_steps'][0]['training']['best_epoch']=9
store['active_learning_steps'][0]['evalution_metrics']={'accuracy': 0.6312, 'crossentropy': 3.4452630039215086}
store['active_learning_steps'][0]['pool_training']={}
store['active_learning_steps'][0]['pool_training']['epochs']=[]
store['active_learning_steps'][0]['pool_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.66712162271142})
store['active_learning_steps'][0]['pool_training']['epochs'].append({'accuracy': 0.617919921875, 'crossentropy': 2.7134549152106047})
store['active_learning_steps'][0]['pool_training']['epochs'].append({'accuracy': 0.61474609375, 'crossentropy': 2.686139814555645})
store['active_learning_steps'][0]['pool_training']['epochs'].append({'accuracy': 0.615478515625, 'crossentropy': 2.473057009279728})
store['active_learning_steps'][0]['pool_training']['epochs'].append({'accuracy': 0.619873046875, 'crossentropy': 2.569880522787571})
store['active_learning_steps'][0]['pool_training']['epochs'].append({'accuracy': 0.617431640625, 'crossentropy': 2.592167327180505})
store['active_learning_steps'][0]['pool_training']['epochs'].append({'accuracy': 0.61572265625, 'crossentropy': 2.585434753447771})
store['active_learning_steps'][0]['pool_training']['best_epoch']=4
store['exception']='Traceback (most recent call last):\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py", line 545, in <module>\n    config.run(store=store)\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py", line 385, in run\n    candidate_batch = self.get_bald_ical_candidate_batch(\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py", line 218, in get_bald_ical_candidate_batch\n    candidate_batch = get_scorers(scores_N, batch_size=self.acquisition_size)\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py", line 389, in <lambda>\n    get_scorers=lambda scores_N, batch_size: get_sampled_tempered_scorers(\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/batchbald.py", line 418, in get_sampled_tempered_scorers\n    candidate_indices = np.random.choice(N, size=batch_size, replace=False, p=p)\n  File "mtrand.pyx", line 930, in numpy.random.mtrand.RandomState.choice\nValueError: probabilities are not non-negative\n'
