store = {}
store['timestamp']=1621200753
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_xmi_labels.py', '--id=3']
store['commit']='e58e22f40eef16250bf8eae7794770660a6579a1'
store['github_url']='e58e22f40eef16250bf8eae7794770660a6579a1'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_xmi_labels.py'
store['job_id']=3
store['worker_id']=3
store['num_workers']=40
store['config']={'seed': 3, 'acquisition_size': 10, 'max_training_set': 300, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 20, 'max_training_epochs': 120, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'initial_set_size': 20, 'min_samples_per_epoch': 1024, 'repeated_mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedCoreSetBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['initial_training_set_indices']=[38043, 40091, 17418, 2094, 39879, 3133, 5011, 40683, 54379, 24287, 9849, 59305, 39508, 39356, 8758, 52579, 13655, 7636, 21562, 41329]
store['dataset_info']={'training': "'FastMNIST (train)' | replace_targets{'targets': tensor([5, 0, 4,  ..., 5, 6, 8], device='cuda:0'), 'num_classes': 10}", 'test': "'FastMNIST (test, 10000 samples)'"}
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.541015625, 'crossentropy': 1.8587678670883179})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.7389668226242065})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.9514161348342896})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.3069114685058594})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.4928035736083984})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.6406896114349365})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.763392686843872})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.775738000869751})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.702360153198242})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.58760142326355})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.6451852321624756})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.675880193710327})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.8069236278533936})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.9765496253967285})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 3.1338725090026855})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 3.015552282333374})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 3.129009246826172})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.9196958541870117})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 3.107146739959717})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.79333233833313})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 3.0015511512756348})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 3.13045597076416})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.966726541519165})
store['active_learning_steps'][0]['training']['best_epoch']=3
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.651, 'crossentropy': 2.1115767578125}
store['exception']='Traceback (most recent call last):\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_xmi_labels.py", line 295, in <module>\n    config.run(store=store)\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_xmi_labels.py", line 217, in run\n    candidate_batch = acquisition_function.compute_candidate_batch(trained_model, pool_loader, self.device)\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/acquisition_functions.py", line 156, in compute_candidate_batch\n    return self.get_candidate_batch(log_probs_N_K_C, labels_N, device)\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/acquisition_functions.py", line 172, in get_candidate_batch\n    candidate_batch = self.extract_candidates(scores_N)\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/acquisition_functions.py", line 191, in extract_candidates\n    return get_sampled_tempered_scorers(scores_N, batch_size=self.acquisition_size, temperature=self.temperature)\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/batchbald.py", line 376, in get_sampled_tempered_scorers\n    candidate_indices = np.random.choice(N, size=batch_size, replace=False, p=p)\n  File "mtrand.pyx", line 919, in numpy.random.mtrand.RandomState.choice\n  File "/scratch-ssd/andsch/tmp/conda_envs/job-6484/lib/python3.8/site-packages/torch/tensor.py", line 623, in __array__\n    return self.numpy().astype(dtype, copy=False)\nTypeError: can\'t convert cuda:0 device type tensor to numpy. Use Tensor.cpu() to copy the tensor to host memory first.\n'
