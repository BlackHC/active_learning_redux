store = {}
store['timestamp']=1610146025
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py', '--id', '57']
store['commit']='466d7e4a4eedcd2b9dd80c52983a524624d138a9'
store['github_url']='466d7e4a4eedcd2b9dd80c52983a524624d138a9'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py'
store['job_id']=57
store['worker_id']=57
store['num_workers']=100
store['config']={'seed': 398, 'acquisition_size': 10, 'max_training_set': 300, 'num_pool_samples': 20, 'num_eval_samples': 4, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 10, 'validation_set_size': 4096, 'initial_set_size': 20, 'samples_per_epoch': 24576, 'repeated_mnist_repetitions': 2, 'add_dataset_noise': True, 'acquisition_function': 'AcquisitionFunction.temperedbaldical', 'save_bald_scores': False, 'temperature': 13}
store['log']={}
store['initial_training_set_indices']=[38043, 40091, 17418, 2094, 39879, 3133, 5011, 40683, 54379, 24287, 9849, 59305, 39508, 39356, 8758, 52579, 13655, 7636, 21562, 41329]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.514404296875, 'crossentropy': 7.096701949834824})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.49853515625, 'crossentropy': 6.712812248617411})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5224609375, 'crossentropy': 7.035285748541355})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.52099609375, 'crossentropy': 6.837695814669132})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5322265625, 'crossentropy': 6.231485616415739})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.515869140625, 'crossentropy': 7.0424555614590645})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.52880859375, 'crossentropy': 6.533566154539585})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.540283203125, 'crossentropy': 6.060590714216232})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.532470703125, 'crossentropy': 5.96362167224288})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.52734375, 'crossentropy': 5.72572772949934})
store['active_learning_steps'][0]['training']['best_epoch']=10
store['active_learning_steps'][0]['evalution_metrics']={'accuracy': 0.5359, 'crossentropy': 5.700553945922851}
store['active_learning_steps'][0]['pool_training']={}
store['active_learning_steps'][0]['pool_training']['epochs']=[]
store['active_learning_steps'][0]['pool_training']['epochs'].append({'accuracy': 0.5361328125, 'crossentropy': 4.8997362069785595})
store['active_learning_steps'][0]['pool_training']['epochs'].append({'accuracy': 0.5302734375, 'crossentropy': 5.394118197262287})
store['active_learning_steps'][0]['pool_training']['epochs'].append({'accuracy': 0.53955078125, 'crossentropy': 5.466763392090797})
store['active_learning_steps'][0]['pool_training']['epochs'].append({'accuracy': 0.53857421875, 'crossentropy': 5.574841797351837})
store['active_learning_steps'][0]['pool_training']['best_epoch']=1
store['exception']='Traceback (most recent call last):\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py", line 545, in <module>\n    config.run(store=store)\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py", line 385, in run\n    candidate_batch = self.get_bald_ical_candidate_batch(\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py", line 218, in get_bald_ical_candidate_batch\n    candidate_batch = get_scorers(scores_N, batch_size=self.acquisition_size)\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py", line 389, in <lambda>\n    get_scorers=lambda scores_N, batch_size: get_sampled_tempered_scorers(\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/batchbald.py", line 418, in get_sampled_tempered_scorers\n    candidate_indices = np.random.choice(N, size=batch_size, replace=False, p=p)\n  File "mtrand.pyx", line 930, in numpy.random.mtrand.RandomState.choice\nValueError: probabilities are not non-negative\n'
