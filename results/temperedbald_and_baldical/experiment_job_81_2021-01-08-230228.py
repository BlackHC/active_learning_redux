store = {}
store['timestamp']=1610146948
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py', '--id', '81']
store['commit']='466d7e4a4eedcd2b9dd80c52983a524624d138a9'
store['github_url']='466d7e4a4eedcd2b9dd80c52983a524624d138a9'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py'
store['job_id']=81
store['worker_id']=81
store['num_workers']=100
store['config']={'seed': 424, 'acquisition_size': 10, 'max_training_set': 300, 'num_pool_samples': 20, 'num_eval_samples': 4, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 10, 'validation_set_size': 4096, 'initial_set_size': 20, 'samples_per_epoch': 24576, 'repeated_mnist_repetitions': 2, 'add_dataset_noise': True, 'acquisition_function': 'AcquisitionFunction.temperedbaldical', 'save_bald_scores': False, 'temperature': 13}
store['log']={}
store['initial_training_set_indices']=[38043, 40091, 17418, 2094, 39879, 3133, 5011, 40683, 54379, 24287, 9849, 59305, 39508, 39356, 8758, 52579, 13655, 7636, 21562, 41329]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.482666015625, 'crossentropy': 8.027953252196312})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.4970703125, 'crossentropy': 7.215041600167751})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.496826171875, 'crossentropy': 6.790559932589531})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.4765625, 'crossentropy': 6.6701036766171455})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.482177734375, 'crossentropy': 7.078825570642948})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.50927734375, 'crossentropy': 7.575451776385307})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.49853515625, 'crossentropy': 6.614319879561663})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.494384765625, 'crossentropy': 6.3891083635389805})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5, 'crossentropy': 6.09034051373601})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.480224609375, 'crossentropy': 7.430419839918613})
store['active_learning_steps'][0]['training']['best_epoch']=9
store['active_learning_steps'][0]['evalution_metrics']={'accuracy': 0.5054, 'crossentropy': 5.847354958343506}
store['active_learning_steps'][0]['pool_training']={}
store['active_learning_steps'][0]['pool_training']['epochs']=[]
store['active_learning_steps'][0]['pool_training']['epochs'].append({'accuracy': 0.486328125, 'crossentropy': 5.77352836355567})
store['active_learning_steps'][0]['pool_training']['epochs'].append({'accuracy': 0.491455078125, 'crossentropy': 5.674901269376278})
store['active_learning_steps'][0]['pool_training']['epochs'].append({'accuracy': 0.481201171875, 'crossentropy': 5.779350228607655})
store['active_learning_steps'][0]['pool_training']['epochs'].append({'accuracy': 0.483154296875, 'crossentropy': 6.045211389660835})
store['active_learning_steps'][0]['pool_training']['epochs'].append({'accuracy': 0.483154296875, 'crossentropy': 5.525768682360649})
store['active_learning_steps'][0]['pool_training']['epochs'].append({'accuracy': 0.4921875, 'crossentropy': 5.320280589163303})
store['active_learning_steps'][0]['pool_training']['epochs'].append({'accuracy': 0.490234375, 'crossentropy': 5.406477220356464})
store['active_learning_steps'][0]['pool_training']['epochs'].append({'accuracy': 0.4814453125, 'crossentropy': 5.45010320097208})
store['active_learning_steps'][0]['pool_training']['epochs'].append({'accuracy': 0.488037109375, 'crossentropy': 5.269215051084757})
store['active_learning_steps'][0]['pool_training']['best_epoch']=9
store['exception']='Traceback (most recent call last):\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py", line 545, in <module>\n    config.run(store=store)\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py", line 385, in run\n    candidate_batch = self.get_bald_ical_candidate_batch(\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py", line 218, in get_bald_ical_candidate_batch\n    candidate_batch = get_scorers(scores_N, batch_size=self.acquisition_size)\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment.py", line 389, in <lambda>\n    get_scorers=lambda scores_N, batch_size: get_sampled_tempered_scorers(\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/batchbald.py", line 418, in get_sampled_tempered_scorers\n    candidate_indices = np.random.choice(N, size=batch_size, replace=False, p=p)\n  File "mtrand.pyx", line 930, in numpy.random.mtrand.RandomState.choice\nValueError: probabilities are not non-negative\n'
