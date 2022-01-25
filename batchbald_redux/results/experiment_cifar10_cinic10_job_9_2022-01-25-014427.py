store = {}
store['timestamp']=1643075067
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_cifar10_cinic10.py', '--id=9']
store['commit']='dc7d3a8288347be382c700aa7edbf186e06ed9cb'
store['github_url']='dc7d3a8288347be382c700aa7edbf186e06ed9cb'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_cifar10_cinic10.py'
store['job_id']=9
store['worker_id']=9
store['num_workers']=18
store['config']={'seed': 8955, 'experiment_data_config': {'id_dataset_name': 'CINIC-10', 'id_repetitions': 1, 'initial_training_set_size': 1000, 'validation_set_size': 1024, 'validation_split_random_state': 0, 'evaluation_set_size': 0, 'add_dataset_noise': False, 'ood_dataset_config': None}, 'acquisition_size': 300, 'max_training_set': 16000, 'max_training_epochs': 105, 'num_pool_samples': 1, 'num_validation_samples': 1, 'num_training_samples': 1, 'device': 'cuda', 'acquisition_function': 'batchbald_redux.acquisition_functions.StochasticBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_trainer_factory': 'batchbald_redux.resnet_models.Cifar10ModelWorkshopPaperTrainer', 'ensemble_size': 3, 'temperature': 1.0, 'coldness': 0.125, 'stochastic_mode': 'StochasticMode.Softmax', 'epig_bootstrap_type': 'BootstrapType.NO_BOOTSTRAP', 'epig_bootstrap_factor': 1.0, 'epig_dtype': torch.float64, 'disable_training_augmentations': False, 'cache_explicit_eval_model': False, 'resnet18_dropout_head': False}
store['log']={}
store['dataset_info']={'training': "'CINIC-10 (Train, imagenet_only=False, seed=0, 178976 samples)'", 'test': "'CINIC-10 (Test, imagenet_only={imagenet_only})'"}
store['initial_training_set_indices']=[76885, 146195, 19213, 53579, 106930, 37164, 101544, 52868, 9447, 71788, 132854, 102855, 76169, 45024, 108569, 112047, 156851, 100142, 168871, 174186, 89287, 137274, 131399, 35140, 80898, 120379, 107556, 91127, 116009, 145812, 112396, 130083, 97631, 126960, 132186, 172262, 23897, 173598, 141088, 70464, 128400, 98690, 73417, 29026, 20683, 10569, 163864, 149002, 167628, 114491, 98704, 145829, 129256, 146892, 107593, 121202, 96762, 136914, 98770, 45839, 10001, 39469, 160323, 51867, 47415, 94499, 22571, 38619, 12784, 43762, 32716, 34021, 41188, 43394, 163255, 68280, 57631, 136796, 41657, 146003, 134271, 101007, 13086, 83267, 14005, 123702, 171664, 34041, 40952, 159164, 118860, 100301, 170731, 40575, 12285, 39431, 168605, 65404, 56632, 48659, 17831, 69715, 72448, 121061, 109967, 36769, 139083, 18440, 167443, 107464, 102647, 85381, 66234, 42266, 159714, 8105, 128548, 120343, 15421, 121937, 171743, 104593, 155018, 151717, 10372, 131365, 42813, 2272, 172838, 161162, 107051, 5066, 133960, 214, 25240, 54094, 151164, 14227, 51269, 174105, 163763, 49991, 49281, 13379, 28342, 1997, 15561, 146689, 41015, 171799, 67484, 87821, 169001, 125729, 168688, 153154, 138282, 17423, 33124, 30723, 138877, 10673, 26639, 172995, 100406, 58903, 77991, 76005, 126169, 167872, 41716, 163849, 63475, 150654, 27193, 177262, 18746, 164187, 13260, 61178, 64917, 156642, 72243, 49660, 151872, 57649, 56759, 122800, 154642, 29802, 123700, 20292, 113908, 40047, 143861, 146125, 125442, 88035, 135890, 175507, 52046, 34954, 53841, 100574, 81109, 49845, 120313, 136838, 114959, 19858, 112044, 78270, 133110, 129403, 34074, 44807, 171602, 167984, 1164, 117377, 91009, 25168, 76935, 172882, 96198, 11880, 83096, 159699, 75417, 29952, 134347, 96287, 10472, 35437, 48800, 60798, 55473, 173495, 158780, 117916, 170912, 141063, 52011, 172521, 124872, 74751, 74693, 36618, 169164, 135757, 75236, 25623, 6506, 98001, 46850, 77577, 67261, 178078, 162730, 57593, 178907, 5694, 6031, 88827, 50154, 32354, 141658, 107860, 154059, 61049, 114338, 83891, 160447, 40681, 177846, 83068, 18259, 111771, 110608, 10097, 37287, 56609, 136435, 114650, 31046, 61155, 22990, 57326, 170995, 61105, 66045, 111499, 25851, 175522, 75711, 69968, 169293, 81696, 104632, 15207, 57721, 137573, 107954, 100648, 68701, 99116, 48866, 175501, 81464, 70700, 147986, 118299, 130400, 94019, 31213, 103592, 77332, 145155, 87094, 2134, 95563, 52767, 47523, 158899, 106837, 48151, 43352, 15667, 23743, 89834, 90767, 98597, 155060, 1994, 110970, 88264, 169876, 100472, 121856, 47909, 157561, 164762, 9766, 174004, 29238, 106764, 87988, 164852, 47915, 23907, 172588, 135310, 151409, 41034, 118150, 81281, 88557, 150663, 112978, 64184, 175782, 123505, 57482, 156462, 96828, 108797, 54694, 128756, 80494, 109972, 79514, 87633, 56277, 162651, 120423, 153497, 96310, 74094, 115562, 81357, 166708, 112363, 9518, 177176, 62659, 107671, 50551, 54347, 172286, 177736, 57237, 86388, 24421, 35020, 15050, 126782, 20934, 15287, 5905, 112004, 74214, 130176, 36705, 90504, 177535, 69783, 93945, 34953, 136768, 149367, 28261, 150530, 134493, 163362, 25544, 46682, 166422, 135450, 161310, 157742, 97555, 37835, 65213, 22000, 59608, 17520, 128457, 88456, 127035, 67601, 131467, 8156, 164042, 29515, 80368, 95796, 27672, 45926, 2148, 162379, 102651, 121561, 162459, 11180, 63249, 18818, 79497, 124968, 153720, 40079, 147681, 89343, 20801, 9494, 62473, 144970, 5040, 139308, 57622, 2969, 1542, 110890, 142822, 80941, 136753, 88668, 9400, 174121, 117075, 76557, 158003, 150903, 133442, 239, 58265, 175086, 88569, 526, 145077, 114795, 164466, 15268, 2891, 74639, 140250, 167421, 68885, 9814, 167225, 170765, 49350, 146545, 35977, 33550, 88216, 29257, 128931, 35958, 54293, 110684, 80435, 43594, 111445, 26940, 129859, 16077, 114639, 71305, 36309, 95324, 121532, 53586, 111974, 125152, 88181, 329, 96380, 138974, 29537, 43380, 29615, 123639, 171552, 107060, 108971, 156933, 111663, 64371, 110671, 112601, 103251, 104444, 148666, 98561, 155, 147140, 163632, 145977, 165826, 77758, 77854, 32729, 79471, 147047, 155895, 167790, 64131, 94963, 91687, 49098, 29336, 94844, 171258, 94490, 940, 66471, 76500, 51557, 25538, 156352, 160254, 159711, 35152, 10622, 23669, 68316, 124956, 152579, 98293, 128718, 156793, 137268, 168538, 2463, 152418, 11316, 82759, 61373, 57499, 111998, 3545, 108406, 70643, 16759, 68669, 138582, 131040, 160957, 77384, 69211, 69106, 41555, 19676, 103831, 9779, 53079, 67435, 172856, 146205, 46149, 29901, 129491, 68821, 53320, 24305, 49608, 109195, 17700, 29014, 81136, 106123, 98526, 11139, 136582, 176321, 162544, 84321, 162737, 124038, 112651, 173536, 171999, 92301, 157679, 74487, 91316, 10401, 128446, 89544, 156693, 55998, 52883, 5165, 129529, 168209, 171338, 26094, 52523, 173680, 76690, 135279, 98598, 76915, 178122, 168657, 151711, 13142, 86061, 124563, 17404, 37655, 69886, 170190, 25926, 97172, 123634, 104991, 22602, 158831, 71415, 81457, 81521, 126454, 9050, 141341, 85382, 53089, 163649, 130572, 42904, 93766, 76307, 76584, 45760, 34625, 120526, 79798, 107978, 98182, 56201, 166167, 23995, 50830, 39240, 53279, 154040, 61679, 118061, 161356, 109923, 138114, 163578, 170600, 127752, 34827, 10775, 13077, 88683, 161400, 115003, 65206, 101518, 8721, 132563, 157315, 98594, 12953, 32773, 82065, 13035, 9359, 75960, 127433, 137297, 167843, 55788, 14292, 23598, 77843, 101220, 166906, 38517, 33360, 104487, 147505, 74126, 83087, 13452, 16201, 165565, 3795, 166766, 53872, 67167, 114377, 13737, 130455, 60093, 167042, 166131, 110629, 130044, 163842, 20298, 56749, 101548, 145213, 78309, 4711, 63300, 17671, 66844, 46596, 147482, 61796, 69583, 19800, 7217, 130835, 17143, 131191, 39357, 176376, 3173, 107403, 160449, 150573, 14926, 139315, 29383, 53641, 40446, 25107, 79792, 118725, 28636, 71340, 89936, 86451, 174690, 91401, 57667, 112400, 74549, 143243, 169543, 99835, 7304, 113399, 143932, 21024, 104415, 97580, 39990, 116262, 29347, 14500, 98114, 159497, 6188, 127293, 174139, 3744, 91976, 118778, 27987, 38791, 108009, 5307, 95171, 146462, 84539, 117495, 81391, 6725, 24715, 162774, 148442, 10471, 6484, 65394, 64922, 131746, 75638, 174297, 1695, 154740, 81278, 66524, 140972, 6748, 29417, 57990, 139695, 128858, 8223, 98567, 171939, 98795, 48411, 97649, 122210, 120441, 57132, 53619, 52757, 161503, 67081, 62926, 73399, 171754, 160211, 64028, 72439, 121529, 85139, 147304, 48814, 95689, 146917, 25081, 28663, 168487, 21610, 140469, 161417, 176135, 126349, 99068, 90242, 77470, 108179, 88275, 5665, 44018, 147007, 44202, 174898, 45820, 8056, 9738, 122671, 125718, 51859, 130658, 160155, 46701, 116779, 158099, 104161, 44147, 61097, 105528, 29958, 109667, 36246, 14055, 70628, 49697, 177496, 123209, 160398, 53034, 11904, 36582, 96908, 40884, 151243, 137287, 124380, 106430, 34935, 71132, 53616, 165602, 70209, 136218, 86888, 81347, 46007, 32519, 27912, 128784, 42942, 35173, 11334, 23391, 97336, 176499, 31754, 69765, 78911, 148312, 58461, 37800, 143741, 125155, 107931, 41441, 34665, 147595, 89238, 55, 95887, 97701, 174201, 156162, 152017, 135726, 72303, 117127, 28103, 127609, 119547, 87138, 172374, 112401, 149829, 72817, 8520, 66072, 97228, 62498, 140482, 60976, 117900, 25733, 53542, 2876, 151513, 117401, 67704, 106151, 60743, 141588, 71166, 104934, 43333, 9086, 97857, 140590, 14499, 171477, 77911, 119510, 113173, 130669, 17056, 150518, 114872, 93077, 167597, 107003, 24166, 28175, 55032, 117602, 26636, 131981, 110157]
store['evaluation_set_indices']=[]
store['seed']=8148459211323306030
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['ensemble']=[]
store['active_learning_steps'][0]['training']['ensemble'].append({})
store['active_learning_steps'][0]['training']['ensemble'][0]['epochs']=[]
store['active_learning_steps'][0]['training']['ensemble'][0]['era_epochs']=[]
store['active_learning_steps'][0]['training']['ensemble'][0]['epochs'].append({'accuracy': 0.1376953125, 'crossentropy': 2.286525011062622})
store['active_learning_steps'][0]['training']['ensemble'][0]['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 2.162208318710327})
store['active_learning_steps'][0]['training']['ensemble'][0]['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 2.0408129692077637})
store['active_learning_steps'][0]['training']['ensemble'][0]['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 1.961986780166626})
store['active_learning_steps'][0]['training']['ensemble'][0]['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 1.9965806007385254})
store['active_learning_steps'][0]['training']['ensemble'][0]['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 2.0254249572753906})
store['active_learning_steps'][0]['training']['ensemble'][0]['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 1.9925140142440796})
store['active_learning_steps'][0]['training']['ensemble'][0]['epochs'].append({'accuracy': 0.25, 'crossentropy': 2.7660303115844727})
store['active_learning_steps'][0]['training']['ensemble'][0]['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 2.028125286102295})
store['active_learning_steps'][0]['training']['ensemble'][0]['epochs'].append({'accuracy': 0.326171875, 'crossentropy': 2.0343971252441406})
store['active_learning_steps'][0]['training']['ensemble'][0]['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 2.0626440048217773})
store['active_learning_steps'][0]['training']['ensemble'][0]['epochs'].append({'accuracy': 0.3447265625, 'crossentropy': 1.8373756408691406})
store['active_learning_steps'][0]['training']['ensemble'][0]['epochs'].append({'accuracy': 0.33984375, 'crossentropy': 2.085909843444824})
store['active_learning_steps'][0]['training']['ensemble'][0]['epochs'].append({'accuracy': 0.341796875, 'crossentropy': 1.9529722929000854})
store['active_learning_steps'][0]['training']['ensemble'][0]['epochs'].append({'accuracy': 0.3330078125, 'crossentropy': 1.9168980121612549})
store['active_learning_steps'][0]['training']['ensemble'][0]['epochs'].append({'accuracy': 0.3330078125, 'crossentropy': 2.037064790725708})
store['active_learning_steps'][0]['training']['ensemble'][0]['epochs'].append({'accuracy': 0.3544921875, 'crossentropy': 2.0784876346588135})
store['active_learning_steps'][0]['training']['ensemble'][0]['epochs'].append({'accuracy': 0.3466796875, 'crossentropy': 2.0024428367614746})
store['active_learning_steps'][0]['training']['ensemble'][0]['epochs'].append({'accuracy': 0.33984375, 'crossentropy': 2.176919937133789})
store['active_learning_steps'][0]['training']['ensemble'][0]['epochs'].append({'accuracy': 0.298828125, 'crossentropy': 2.2408857345581055})
store['active_learning_steps'][0]['training']['ensemble'][0]['epochs'].append({'accuracy': 0.3583984375, 'crossentropy': 2.133734703063965})
store['active_learning_steps'][0]['training']['ensemble'][0]['epochs'].append({'accuracy': 0.34375, 'crossentropy': 2.1067962646484375})
store['active_learning_steps'][0]['training']['ensemble'][0]['epochs'].append({'accuracy': 0.369140625, 'crossentropy': 2.3092267513275146})
store['active_learning_steps'][0]['training']['ensemble'][0]['epochs'].append({'accuracy': 0.353515625, 'crossentropy': 2.155534505844116})
store['active_learning_steps'][0]['training']['ensemble'][0]['epochs'].append({'accuracy': 0.361328125, 'crossentropy': 2.071728229522705})
store['active_learning_steps'][0]['training']['ensemble'][0]['epochs'].append({'accuracy': 0.3603515625, 'crossentropy': 2.5172653198242188})
store['active_learning_steps'][0]['training']['ensemble'][0]['epochs'].append({'accuracy': 0.3583984375, 'crossentropy': 2.287121057510376})
store['active_learning_steps'][0]['training']['ensemble'][0]['epochs'].append({'accuracy': 0.375, 'crossentropy': 2.264101266860962})
store['active_learning_steps'][0]['training']['ensemble'][0]['epochs'].append({'accuracy': 0.3466796875, 'crossentropy': 2.3578906059265137})
store['active_learning_steps'][0]['training']['ensemble'][0]['epochs'].append({'accuracy': 0.3505859375, 'crossentropy': 2.607470989227295})
store['active_learning_steps'][0]['training']['ensemble'][0]['epochs'].append({'accuracy': 0.330078125, 'crossentropy': 2.725018262863159})
store['active_learning_steps'][0]['training']['ensemble'][0]['epochs'].append({'accuracy': 0.34765625, 'crossentropy': 2.552809238433838})
store['active_learning_steps'][0]['training']['ensemble'][0]['epochs'].append({'accuracy': 0.380859375, 'crossentropy': 2.412855386734009})
store['active_learning_steps'][0]['training']['ensemble'][0]['epochs'].append({'accuracy': 0.3603515625, 'crossentropy': 2.40096378326416})
store['active_learning_steps'][0]['training']['ensemble'][0]['epochs'].append({'accuracy': 0.3232421875, 'crossentropy': 2.8341455459594727})
store['active_learning_steps'][0]['training']['ensemble'][0]['epochs'].append({'accuracy': 0.3134765625, 'crossentropy': 2.90120267868042})
store['active_learning_steps'][0]['training']['ensemble'][0]['epochs'].append({'accuracy': 0.349609375, 'crossentropy': 2.709688425064087})
store['exception']='Traceback (most recent call last):\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_cifar10_cinic10.py", line 208, in <module>\n    config.run(store=store)\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/unified_experiment.py", line 271, in run\n    active_learner(store)\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/unified_experiment.py", line 106, in __call__\n    trained_model = model_trainer.get_trained(\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/trained_model.py", line 254, in get_trained\n    model = self.model_trainer.get_trained(\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/resnet_models.py", line 448, in get_trained\n    train_with_schedule(\n  File "/auto/users/andsch/github/active_learning_redux/batchbald_redux/black_box_model_training.py", line 269, in train_with_schedule\n    trainer.run(train_loader, max_epochs=max_epochs)\n  File "/scratch-ssd/andsch/tmp/conda_envs/job-29004/lib/python3.8/site-packages/ignite/engine/engine.py", line 704, in run\n    return self._internal_run()\n  File "/scratch-ssd/andsch/tmp/conda_envs/job-29004/lib/python3.8/site-packages/ignite/engine/engine.py", line 783, in _internal_run\n    self._handle_exception(e)\n  File "/scratch-ssd/andsch/tmp/conda_envs/job-29004/lib/python3.8/site-packages/ignite/engine/engine.py", line 466, in _handle_exception\n    raise e\n  File "/scratch-ssd/andsch/tmp/conda_envs/job-29004/lib/python3.8/site-packages/ignite/engine/engine.py", line 753, in _internal_run\n    time_taken = self._run_once_on_dataset()\n  File "/scratch-ssd/andsch/tmp/conda_envs/job-29004/lib/python3.8/site-packages/ignite/engine/engine.py", line 854, in _run_once_on_dataset\n    self._handle_exception(e)\n  File "/scratch-ssd/andsch/tmp/conda_envs/job-29004/lib/python3.8/site-packages/ignite/engine/engine.py", line 466, in _handle_exception\n    raise e\n  File "/scratch-ssd/andsch/tmp/conda_envs/job-29004/lib/python3.8/site-packages/ignite/engine/engine.py", line 840, in _run_once_on_dataset\n    self.state.output = self._process_function(self, self.state.batch)\n  File "/scratch-ssd/andsch/tmp/conda_envs/job-29004/lib/python3.8/site-packages/ignite/engine/__init__.py", line 100, in update\n    y_pred = model(x)\n  File "/scratch-ssd/andsch/tmp/conda_envs/job-29004/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1102, in _call_impl\n    return forward_call(*input, **kwargs)\n  File "/scratch-ssd/andsch/tmp/conda_envs/job-29004/lib/python3.8/site-packages/torch/nn/modules/container.py", line 141, in forward\n    input = module(input)\n  File "/scratch-ssd/andsch/tmp/conda_envs/job-29004/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1102, in _call_impl\n    return forward_call(*input, **kwargs)\n  File "/scratch-ssd/andsch/tmp/conda_envs/job-29004/lib/python3.8/site-packages/torch/nn/modules/container.py", line 141, in forward\n    input = module(input)\n  File "/scratch-ssd/andsch/tmp/conda_envs/job-29004/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1102, in _call_impl\n    return forward_call(*input, **kwargs)\n  File "/scratch-ssd/andsch/tmp/conda_envs/job-29004/lib/python3.8/site-packages/kornia/augmentation/augmentation.py", line 1083, in forward\n    out = super().forward(_input, params, return_transform)\n  File "/scratch-ssd/andsch/tmp/conda_envs/job-29004/lib/python3.8/site-packages/kornia/augmentation/base.py", line 270, in forward\n    output = self.apply_func(in_tensor, in_transform, self._params, return_transform)\n  File "/scratch-ssd/andsch/tmp/conda_envs/job-29004/lib/python3.8/site-packages/kornia/augmentation/base.py", line 228, in apply_func\n    trans_matrix = self.compute_transformation(in_tensor, params)\n  File "/scratch-ssd/andsch/tmp/conda_envs/job-29004/lib/python3.8/site-packages/kornia/augmentation/augmentation.py", line 1005, in compute_transformation\n    transform: torch.Tensor = get_perspective_transform(params["src"].to(input), params["dst"].to(input))\n  File "/scratch-ssd/andsch/tmp/conda_envs/job-29004/lib/python3.8/site-packages/kornia/geometry/transform/imgwarp.py", line 363, in get_perspective_transform\n    X, _ = _torch_solve_cast(b, A)\n  File "/scratch-ssd/andsch/tmp/conda_envs/job-29004/lib/python3.8/site-packages/kornia/utils/helpers.py", line 124, in _torch_solve_cast\n    out = solve(A.to(dtype), input.to(dtype))\nRuntimeError: CUDA error: misaligned address\nCUDA kernel errors might be asynchronously reported at some other API call,so the stacktrace below might be incorrect.\nFor debugging consider passing CUDA_LAUNCH_BLOCKING=1.\n'
