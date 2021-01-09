store = {}
store['timestamp']=1610146745
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py', '--id', '78']
store['commit']='466d7e4a4eedcd2b9dd80c52983a524624d138a9'
store['github_url']='466d7e4a4eedcd2b9dd80c52983a524624d138a9'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py'
store['job_id']=78
store['worker_id']=78
store['num_workers']=100
store['config']={'seed': 421, 'acquisition_size': 5, 'max_training_set': 300, 'num_pool_samples': 20, 'num_eval_samples': 4, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 10, 'validation_set_size': 4096, 'initial_set_size': 20, 'samples_per_epoch': 24576, 'repeated_mnist_repetitions': 2, 'add_dataset_noise': True, 'acquisition_function': 'AcquisitionFunction.temperedbaldical', 'save_bald_scores': False, 'temperature': 13}
store['log']={}
store['initial_training_set_indices']=[38043, 40091, 17418, 2094, 39879, 3133, 5011, 40683, 54379, 24287, 9849, 59305, 39508, 39356, 8758, 52579, 13655, 7636, 21562, 41329]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.485595703125, 'crossentropy': 8.887913219630718})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.480712890625, 'crossentropy': 8.34372729063034})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.46923828125, 'crossentropy': 8.07659763097763})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.475830078125, 'crossentropy': 8.556202739477158})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.471923828125, 'crossentropy': 10.171133644878864})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.487060546875, 'crossentropy': 8.058668717741966})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.478515625, 'crossentropy': 8.568274289369583})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.477783203125, 'crossentropy': 8.046044133603573})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.450439453125, 'crossentropy': 7.71142702549696})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.47802734375, 'crossentropy': 9.009436011314392})
store['active_learning_steps'][0]['training']['best_epoch']=9
store['active_learning_steps'][0]['evalution_metrics']={'accuracy': 0.4521, 'crossentropy': 7.970773931884765}
store['active_learning_steps'][0]['pool_training']={}
store['active_learning_steps'][0]['pool_training']['epochs']=[]
store['active_learning_steps'][0]['pool_training']['epochs'].append({'accuracy': 0.481201171875, 'crossentropy': 6.15103330090642})
store['active_learning_steps'][0]['pool_training']['epochs'].append({'accuracy': 0.475341796875, 'crossentropy': 7.170738037675619})
store['active_learning_steps'][0]['pool_training']['epochs'].append({'accuracy': 0.471923828125, 'crossentropy': 6.977231342345476})
store['active_learning_steps'][0]['pool_training']['epochs'].append({'accuracy': 0.477294921875, 'crossentropy': 7.1728415340185165})
store['active_learning_steps'][0]['pool_training']['best_epoch']=1
store['exception']='Traceback (most recent call last):\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py", line 545, in <module>\n    config.run(store=store)\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py", line 385, in run\n    candidate_batch = self.get_bald_ical_candidate_batch(\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py", line 218, in get_bald_ical_candidate_batch\n    candidate_batch = get_scorers(scores_N, batch_size=self.acquisition_size)\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py", line 389, in <lambda>\n    get_scorers=lambda scores_N, batch_size: get_sampled_tempered_scorers(\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/batchbald.py", line 418, in get_sampled_tempered_scorers\n    candidate_indices = np.random.choice(N, size=batch_size, replace=False, p=p)\n  File "mtrand.pyx", line 930, in numpy.random.mtrand.RandomState.choice\nValueError: probabilities are not non-negative\n'