store = {}
store['timestamp']=1620916181
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=16']
store['commit']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['github_url']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=16
store['worker_id']=16
store['num_workers']=20
store['config']={'seed': 1258, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 100, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.18837571144104})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.682811737060547})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.9211511611938477})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.765324592590332})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6816, 'crossentropy': 1.994144921875}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.196800947189331})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.1787054538726807})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.1686885356903076})
store['active_learning_steps'][0]['eval_training']['best_epoch']=3
store['active_learning_steps'][0]['acquisition']={'indices': [12620, 39483, 30519, 31140, 33193, 6943, 35103, 20037, 7948, 22803], 'labels': [2, 0, 8, 3, 8, 8, 8, 8, 0, 6], 'scores': [0.57781583070755, 0.771425724029541, 0.8775858879089355, 0.6941295862197876, 0.7500922679901123, 0.7361165881156921, 0.7612044215202332, 0.8568929433822632, 0.8396205902099609, 0.5365777611732483]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.835556149482727})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.115769386291504})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.340085983276367})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 2.4356884956359863})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7263, 'crossentropy': 1.649898828125}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.0679666996002197})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.0298714637756348})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 0.9902223348617554})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [5621, 50320, 10321, 53958, 1497, 23619, 33196, 43745, 30079, 10275], 'labels': [3, 5, 2, 3, 1, 9, 7, 8, 4, 6], 'scores': [0.6761912107467651, 0.7012988328933716, 0.4828094244003296, 0.6123186349868774, 0.5573803186416626, 0.5303964614868164, 0.6054465174674988, 0.4444793462753296, 0.5308669805526733, 0.6966390609741211]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.6015689373016357})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.7831060886383057})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.133726119995117})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 2.041224956512451})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7531, 'crossentropy': 1.46333974609375}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.091367244720459})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.0103936195373535})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 0.9865766167640686})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [15757, 16190, 35434, 22883, 4032, 19809, 59656, 49335, 32729, 44501], 'labels': [8, 3, -1, 3, 9, 7, 9, 9, 9, 5], 'scores': [0.5274712443351746, 0.6087896227836609, 0.28407323360443115, 0.6314077377319336, 0.5567491054534912, 0.6441366076469421, 0.5872832536697388, 0.5952415466308594, 0.5018114447593689, 0.4173903465270996]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.2415090799331665})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.343829870223999})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.4866724014282227})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.5556256771087646})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7788, 'crossentropy': 1.1534857421875}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 0.8886237740516663})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 0.8281275033950806})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 0.8351714611053467})
store['active_learning_steps'][3]['eval_training']['best_epoch']=2
store['active_learning_steps'][3]['acquisition']={'indices': [5740, 24097, 31277, 31243, 36473, 56828, 51511, 55648, 58360, 12697], 'labels': [9, 5, 0, 0, 8, 7, 5, 9, 0, 5], 'scores': [0.6729461550712585, 0.588830828666687, 0.6503921151161194, 0.741732120513916, 0.5508143901824951, 0.4297429919242859, 0.3228737413883209, 0.575677752494812, 0.6308964490890503, 0.5169434547424316]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.0038113594055176})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.1429593563079834})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.3003573417663574})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.238250494003296})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7981, 'crossentropy': 0.9862033203125}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 0.9235251545906067})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 0.8286226987838745})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 0.8038010597229004})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [48595, 4997, 44804, 34280, 53441, 16883, 43213, 18001, 10235, 48529], 'labels': [4, 2, 5, 9, 7, 8, 7, 3, 9, 0], 'scores': [0.3993873596191406, 0.40717172622680664, 0.26756221055984497, 0.28932666778564453, 0.4373721480369568, 0.28272008895874023, 0.45102107524871826, 0.408471941947937, 0.4457913637161255, 0.4805114269256592]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8517392873764038})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8762744665145874})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.0235084295272827})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9550849199295044})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8522, 'crossentropy': 0.8446578125}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8100413084030151})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7200673818588257})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.693597674369812})
store['active_learning_steps'][5]['eval_training']['best_epoch']=3
store['active_learning_steps'][5]['acquisition']={'indices': [9428, 20903, 52891, 11202, 35540, 42869, 4723, 48475, 42180, 59637], 'labels': [9, 3, 3, 9, 6, 6, 5, 8, 0, 6], 'scores': [0.7338989973068237, 0.5208206176757812, 0.555760383605957, 0.5160993337631226, 0.4975987672805786, 0.3869873881340027, 0.5560018420219421, 0.3684505224227905, 0.541649580001831, 0.5075204372406006]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.8903717994689941})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8415029048919678})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.939123809337616})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8730179071426392})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.9974613189697266})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8788, 'crossentropy': 0.8333494140625}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7207509279251099})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6047585606575012})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5614942908287048})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5177940726280212})
store['active_learning_steps'][6]['eval_training']['best_epoch']=4
store['active_learning_steps'][6]['acquisition']={'indices': [30289, 24207, 42216, 19464, 49064, 33295, 21242, 14343, 2034, 1618], 'labels': [-1, -1, 4, -1, 8, 1, 0, 2, 4, 7], 'scores': [0.5446984767913818, 0.2555476427078247, 0.6481364369392395, 0.381123423576355, 0.6830391883850098, 0.5058320760726929, 0.6760647296905518, 0.656080961227417, 0.6043993830680847, 0.5966589450836182]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7606213092803955})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6820381879806519})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7755967378616333})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.74909508228302})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8190183639526367})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8934, 'crossentropy': 0.6729482421875}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7372307777404785})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.5782368183135986})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.5597250461578369})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.5730165243148804})
store['active_learning_steps'][7]['eval_training']['best_epoch']=3
store['active_learning_steps'][7]['acquisition']={'indices': [14563, 30367, 8025, 3232, 27073, 12223, 27299, 27199, 15767, 7919], 'labels': [-1, -1, 2, -1, 2, 2, 8, 7, 5, 4], 'scores': [0.4472159147262573, 0.3701200485229492, 0.6517738103866577, 0.2861778140068054, 0.3615040183067322, 0.5809332728385925, 0.46851015090942383, 0.3868158459663391, 0.5291035175323486, 0.35622638463974]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.763840913772583})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6793999671936035})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7819346189498901})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7049282789230347})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7604743242263794})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.9015, 'crossentropy': 0.64415986328125}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6896953582763672})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5622293949127197})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5053085088729858})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.47916337847709656})
store['active_learning_steps'][8]['eval_training']['best_epoch']=4
store['active_learning_steps'][8]['acquisition']={'indices': [20585, 45804, 58720, 13755, 7375, 52823, 21297, 43055, 28066, 41549], 'labels': [4, 7, -1, 7, 2, 4, 9, 5, 6, 7], 'scores': [0.39845335483551025, 0.36922168731689453, 0.43078529834747314, 0.6223215460777283, 0.38490718603134155, 0.2301536202430725, 0.5464532971382141, 0.6376659870147705, 0.3864842653274536, 0.5404430627822876]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7192963361740112})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6469871997833252})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6315789222717285})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6127526760101318})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6832125186920166})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6815648078918457})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6628804206848145})
store['active_learning_steps'][9]['training']['best_epoch']=4
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.9161, 'crossentropy': 0.62354091796875}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6832248568534851})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.49886631965637207})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.46773582696914673})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.4529498815536499})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4075779616832733})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.4278947710990906})
store['active_learning_steps'][9]['eval_training']['best_epoch']=5
store['active_learning_steps'][9]['acquisition']={'indices': [8998, 14815, 51432, 37512, 20630, 27783, 9633, 46248, 18720, 7140], 'labels': [9, 9, 1, 8, 8, 3, 9, 7, 7, 2], 'scores': [0.5833341479301453, 0.5491228103637695, 0.580120325088501, 0.7021886706352234, 0.5558243989944458, 0.4970274567604065, 0.6395650506019592, 0.4676041603088379, 0.6220243573188782, 0.6681720018386841]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7198507189750671})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5654903650283813})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6000939607620239})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5871137380599976})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5295731425285339})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5989049673080444})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6086838245391846})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.668939471244812})
store['active_learning_steps'][10]['training']['best_epoch']=5
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.9302, 'crossentropy': 0.55837060546875}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6575078964233398})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.49455535411834717})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.46413177251815796})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.40521812438964844})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.3922404646873474})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.39604276418685913})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.3911646008491516})
store['active_learning_steps'][10]['eval_training']['best_epoch']=7
store['active_learning_steps'][10]['acquisition']={'indices': [12937, 29190, 38397, 24893, 6819, 15852, 41424, 50370, 25917, 48634], 'labels': [5, -1, -1, -1, -1, -1, -1, 7, -1, -1], 'scores': [0.7373569011688232, 0.6840797662734985, 0.7696313858032227, 0.5377384424209595, 0.6532323956489563, 0.6331167817115784, 0.4867587089538574, 0.7071349620819092, 0.38303232192993164, 0.5378851890563965]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7312023639678955})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5442547798156738})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5532922744750977})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6006375551223755})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5858656167984009})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.9272, 'crossentropy': 0.494833056640625}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7200225591659546})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5107895135879517})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4321850538253784})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4495229721069336})
store['active_learning_steps'][11]['eval_training']['best_epoch']=3
store['active_learning_steps'][11]['acquisition']={'indices': [50410, 54880, 13476, 7386, 38314, 32276, 25341, 4767, 15969, 22030], 'labels': [8, 5, 8, 7, 5, 3, 8, 8, 5, 5], 'scores': [0.311667799949646, 0.4296202063560486, 0.3408162593841553, 0.3556027412414551, 0.49828577041625977, 0.6759204864501953, 0.5127580165863037, 0.6507709622383118, 0.36940228939056396, 0.4292716979980469]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7926139235496521})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5551875829696655})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5882737636566162})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5547550916671753})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7124516367912292})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6293889284133911})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7067862749099731})
store['active_learning_steps'][12]['training']['best_epoch']=4
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9319, 'crossentropy': 0.50608837890625}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6901367902755737})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4932628870010376})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.4653123617172241})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4511975646018982})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.416646271944046})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4258352518081665})
store['active_learning_steps'][12]['eval_training']['best_epoch']=5
store['active_learning_steps'][12]['acquisition']={'indices': [39016, 22895, 35070, 28657, 39031, 5171, 3382, 826, 14332, 34688], 'labels': [9, 9, 9, 5, 2, 2, 9, 9, 9, 9], 'scores': [0.7879746556282043, 0.5819188952445984, 0.6298998594284058, 0.41410553455352783, 0.42830222845077515, 0.5075550675392151, 0.6043890714645386, 0.689235270023346, 0.669339507818222, 0.5782582759857178]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7874352931976318})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6040261387825012})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5304538011550903})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6141067743301392})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6046500205993652})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5628047585487366})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9328, 'crossentropy': 0.51144775390625}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7246806621551514})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5174659490585327})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.4931867718696594})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.40983644127845764})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.41212406754493713})
store['active_learning_steps'][13]['eval_training']['best_epoch']=4
store['active_learning_steps'][13]['acquisition']={'indices': [4749, 38256, 16822, 45073, 41242, 7967, 52514, 45931, 40392, 59872], 'labels': [0, 2, 6, 2, -1, -1, 6, -1, 4, -1], 'scores': [0.6118796467781067, 0.47452157735824585, 0.7013612985610962, 0.6890470385551453, 0.45843029022216797, 0.4275858998298645, 0.7189010381698608, 0.22778189182281494, 0.4346996545791626, 0.5018722414970398]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8611490726470947})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5709157586097717})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5226414203643799})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5364015102386475})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.502117931842804})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5296427011489868})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5766862034797668})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6420259475708008})
store['active_learning_steps'][14]['training']['best_epoch']=5
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9364, 'crossentropy': 0.48428251953125}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6638067960739136})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4182254672050476})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.39323121309280396})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3584595322608948})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3733159899711609})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3409017324447632})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3412180244922638})
store['active_learning_steps'][14]['eval_training']['best_epoch']=6
store['active_learning_steps'][14]['acquisition']={'indices': [14901, 27935, 32438, 5317, 59726, 38559, 43961, 59303, 33057, 48427], 'labels': [2, -1, 2, -1, -1, 0, 0, 8, 7, -1], 'scores': [0.5827480554580688, 0.4141730070114136, 0.45753762125968933, 0.38786041736602783, 0.47370827198028564, 0.5899152755737305, 0.7255337238311768, 0.647670328617096, 0.5233648419380188, 0.2708430290222168]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7845180034637451})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5473882555961609})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4995569586753845})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.495471328496933})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5165180563926697})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5942094326019287})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5380904674530029})
store['active_learning_steps'][15]['training']['best_epoch']=4
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9377, 'crossentropy': 0.463185400390625}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7121138572692871})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4256020486354828})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.42031389474868774})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.3770008385181427})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3695308268070221})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3545687794685364})
store['active_learning_steps'][15]['eval_training']['best_epoch']=6
store['active_learning_steps'][15]['acquisition']={'indices': [24312, 38894, 12109, 11747, 22631, 459, 7350, 15332, 23923, 22844], 'labels': [-1, 3, -1, 3, 3, -1, 4, 3, -1, -1], 'scores': [0.37940526008605957, 0.4075574576854706, 0.1955932378768921, 0.4041213393211365, 0.5330180823802948, 0.6094231605529785, 0.41087692975997925, 0.5739269852638245, 0.3302586078643799, 0.4099142551422119]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.9438967704772949})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.503198504447937})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5119078159332275})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.49365371465682983})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.46081027388572693})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5159524083137512})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5154571533203125})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5694315433502197})
store['active_learning_steps'][16]['training']['best_epoch']=5
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9396, 'crossentropy': 0.459933935546875}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7881196737289429})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.45445743203163147})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.402282178401947})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3672974407672882})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3591480255126953})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.361892968416214})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3483569324016571})
store['active_learning_steps'][16]['eval_training']['best_epoch']=7
store['active_learning_steps'][16]['acquisition']={'indices': [3211, 6389, 37050, 49066, 18946, 29928, 25819, 12309, 10824, 53102], 'labels': [-1, -1, 6, 6, 2, -1, -1, -1, 2, -1], 'scores': [0.37005019187927246, 0.4055870771408081, 0.5004784762859344, 0.47974711656570435, 0.32264214754104614, 0.44451743364334106, 0.4492589235305786, 0.39912474155426025, 0.40947359800338745, 0.48885977268218994]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.9995170831680298})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5317516326904297})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.49649345874786377})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.48443639278411865})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4855380356311798})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.48125267028808594})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4708527624607086})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5331485271453857})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5113439559936523})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.510129451751709})
store['active_learning_steps'][17]['training']['best_epoch']=7
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9479, 'crossentropy': 0.440392333984375}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6913757920265198})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.44876188039779663})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3930274248123169})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3374914526939392})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.32531046867370605})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3356267809867859})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.31753790378570557})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3159441351890564})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.321869432926178})
store['active_learning_steps'][17]['eval_training']['best_epoch']=8
store['active_learning_steps'][17]['acquisition']={'indices': [86, 24892, 45744, 45776, 50960, 12880, 1796, 20900, 22735, 21636], 'labels': [-1, -1, 7, 7, -1, -1, -1, 9, -1, -1], 'scores': [0.4004228711128235, 0.4086507558822632, 0.5893954932689667, 0.36491507291793823, 0.6023269891738892, 0.655055046081543, 0.4673035144805908, 0.513843297958374, 0.4170764684677124, 0.5248357057571411]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7602134943008423})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.49665528535842896})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.471108078956604})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.45519018173217773})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5139629244804382})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5109907388687134})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5269829630851746})
store['active_learning_steps'][18]['training']['best_epoch']=4
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9449, 'crossentropy': 0.434371630859375}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6842478513717651})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.43534812331199646})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.40257972478866577})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3666011095046997})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.36574822664260864})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3492293059825897})
store['active_learning_steps'][18]['eval_training']['best_epoch']=6
store['active_learning_steps'][18]['acquisition']={'indices': [21889, 49522, 6913, 31293, 13030, 52169, 36822, 50195, 57076, 5474], 'labels': [1, 8, -1, 8, 0, 2, 1, -1, 4, 8], 'scores': [0.368685781955719, 0.5812249779701233, 0.3236815929412842, 0.6259325742721558, 0.7727985382080078, 0.5338154435157776, 0.49430322647094727, 0.3725001811981201, 0.37234705686569214, 0.5682833194732666]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8411723971366882})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5972347259521484})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5013418793678284})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.47199124097824097})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5893783569335938})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5299965143203735})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5531052350997925})
store['active_learning_steps'][19]['training']['best_epoch']=4
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9367, 'crossentropy': 0.43897841796875}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.687114953994751})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.44975781440734863})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.47976112365722656})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4145825207233429})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.40049660205841064})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3878476023674011})
store['active_learning_steps'][19]['eval_training']['best_epoch']=6
store['active_learning_steps'][19]['acquisition']={'indices': [34445, 55232, 46890, 54628, 3300, 17294, 45529, 4043, 54814, 42386], 'labels': [7, -1, 5, 4, -1, 5, 8, -1, 4, -1], 'scores': [0.454344779253006, 0.23847782611846924, 0.39828306436538696, 0.46217799186706543, 0.41408318281173706, 0.4722369313240051, 0.5071245431900024, 0.531949520111084, 0.4973411560058594, 0.4815385341644287]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8522929549217224})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5125666856765747})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4632759988307953})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.45004212856292725})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.43508511781692505})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4562983512878418})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.45124226808547974})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.48160216212272644})
store['active_learning_steps'][20]['training']['best_epoch']=5
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9527, 'crossentropy': 0.38134130859375}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.702917218208313})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4431779384613037})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.41164541244506836})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.33165866136550903})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.34098225831985474})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3484124541282654})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3152727782726288})
store['active_learning_steps'][20]['eval_training']['best_epoch']=7
store['active_learning_steps'][20]['acquisition']={'indices': [13850, 36126, 34872, 9677, 6582, 57756, 58560, 42904, 43349, 8877], 'labels': [-1, 5, 8, 0, 8, -1, 0, 6, -1, -1], 'scores': [0.41416001319885254, 0.6400046348571777, 0.46136850118637085, 0.5494273900985718, 0.4366481304168701, 0.33656197786331177, 0.6767596006393433, 0.40464890003204346, 0.24703872203826904, 0.39579713344573975]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.9668608903884888})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5628350973129272})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5351756811141968})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.551028847694397})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.49913811683654785})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5893034934997559})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5744093656539917})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6415664553642273})
store['active_learning_steps'][21]['training']['best_epoch']=5
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9411, 'crossentropy': 0.447759228515625}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7368263006210327})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5193567276000977})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.42406511306762695})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3656459450721741})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3645312786102295})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3845173716545105})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3785097599029541})
store['active_learning_steps'][21]['eval_training']['best_epoch']=5
store['active_learning_steps'][21]['acquisition']={'indices': [34587, 27703, 28770, 48297, 12377, 56302, 48499, 49910, 24452, 15505], 'labels': [3, 6, 5, 9, 3, 4, -1, 6, 3, -1], 'scores': [0.408063679933548, 0.6297222375869751, 0.5428295135498047, 0.3340897560119629, 0.5659546256065369, 0.6825945377349854, 0.39991676807403564, 0.3728545308113098, 0.43355292081832886, 0.42960643768310547]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8188447952270508})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5225269198417664})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4533080458641052})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.45713892579078674})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4644430875778198})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.48281487822532654})
store['active_learning_steps'][22]['training']['best_epoch']=3
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9371, 'crossentropy': 0.457354150390625}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.713573694229126})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.47248995304107666})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.40136998891830444})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.38153940439224243})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.40063750743865967})
store['active_learning_steps'][22]['eval_training']['best_epoch']=4
store['active_learning_steps'][22]['acquisition']={'indices': [56014, 12555, 13800, 31251, 23991, 44295, 39304, 1219, 10211, 23421], 'labels': [5, 0, 5, -1, -1, 3, 4, 8, 5, -1], 'scores': [0.5319671034812927, 0.5159878730773926, 0.34308674931526184, 0.3839397430419922, 0.23182010650634766, 0.49165642261505127, 0.4877576231956482, 0.43575477600097656, 0.27306777238845825, 0.33261096477508545]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.9052464365959167})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5580258965492249})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5130298733711243})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5325000882148743})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5612519979476929})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5400187969207764})
store['active_learning_steps'][23]['training']['best_epoch']=3
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9336, 'crossentropy': 0.450437841796875}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7569799423217773})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5153070688247681})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.43745896220207214})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.406715452671051})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.39413928985595703})
store['active_learning_steps'][23]['eval_training']['best_epoch']=5
store['active_learning_steps'][23]['acquisition']={'indices': [44079, 41387, 10064, 2901, 48482, 12332, 5636, 24992, 39275, 9002], 'labels': [1, 5, 8, -1, -1, 4, -1, 4, -1, 9], 'scores': [0.4202805161476135, 0.4137849807739258, 0.7016099095344543, 0.33476686477661133, 0.3214155435562134, 0.5847781598567963, 0.2902225852012634, 0.49046790599823, 0.27915704250335693, 0.3123728036880493]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.9717696905136108})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6190742254257202})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5216723084449768})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5138999223709106})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5441280007362366})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.49910104274749756})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.562080979347229})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5529636144638062})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5368533134460449})
store['active_learning_steps'][24]['training']['best_epoch']=6
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9396, 'crossentropy': 0.427065673828125}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7697932720184326})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.45850810408592224})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.408063143491745})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.35250282287597656})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.36133426427841187})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.38013291358947754})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.360437273979187})
store['active_learning_steps'][24]['eval_training']['best_epoch']=4
store['active_learning_steps'][24]['acquisition']={'indices': [52014, 33598, 57586, 14852, 39940, 12187, 32577, 12791, 5708, 44738], 'labels': [3, -1, -1, 2, -1, -1, -1, 1, -1, -1], 'scores': [0.4334459900856018, 0.43818503618240356, 0.5756810903549194, 0.5008572936058044, 0.45728570222854614, 0.4289281368255615, 0.3646494746208191, 0.3132544755935669, 0.3889056444168091, 0.5461814403533936]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.97925865650177})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5163149833679199})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4427488446235657})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.46658632159233093})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4420614540576935})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5094138383865356})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5198878645896912})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5292537212371826})
store['active_learning_steps'][25]['training']['best_epoch']=5
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9446, 'crossentropy': 0.395964990234375}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7335835695266724})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.47306203842163086})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4198128581047058})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.39305758476257324})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.36295726895332336})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3543051481246948})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.328401118516922})
store['active_learning_steps'][25]['eval_training']['best_epoch']=7
store['active_learning_steps'][25]['acquisition']={'indices': [16951, 56532, 29206, 41017, 28338, 44360, 57156, 45944, 49688, 6836], 'labels': [8, -1, 4, 8, -1, 8, 5, 9, 4, 5], 'scores': [0.6545601487159729, 0.2730015516281128, 0.3769870400428772, 0.5227835178375244, 0.31094276905059814, 0.37130045890808105, 0.3286135196685791, 0.49310624599456787, 0.431569904088974, 0.45710474252700806]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8363823890686035})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5122120380401611})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4027789235115051})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4780076742172241})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.45225438475608826})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4695434272289276})
store['active_learning_steps'][26]['training']['best_epoch']=3
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9457, 'crossentropy': 0.3882611328125}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7207326889038086})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4803904891014099})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4275994300842285})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.37140679359436035})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.37291955947875977})
store['active_learning_steps'][26]['eval_training']['best_epoch']=4
store['active_learning_steps'][26]['acquisition']={'indices': [33338, 29376, 52740, 25823, 22991, 55285, 715, 51004, 7705, 17409], 'labels': [-1, -1, -1, 0, -1, -1, -1, 7, -1, 3], 'scores': [0.43497639894485474, 0.4695591330528259, 0.3198368549346924, 0.42575863003730774, 0.4808809757232666, 0.4914836883544922, 0.24389100074768066, 0.5094456076622009, 0.3008458614349365, 0.48156803846359253]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9761378765106201})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5323631167411804})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4189925789833069})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4564598798751831})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.46613287925720215})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.46904313564300537})
store['active_learning_steps'][27]['training']['best_epoch']=3
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9459, 'crossentropy': 0.4011337890625}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7406880855560303})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4939691126346588})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.41706788539886475})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4249017834663391})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4051702320575714})
store['active_learning_steps'][27]['eval_training']['best_epoch']=5
store['active_learning_steps'][27]['acquisition']={'indices': [26752, 26048, 11495, 30723, 41445, 54573, 6390, 56738, 9944, 7851], 'labels': [5, 3, -1, -1, 0, 2, 8, -1, 8, 8], 'scores': [0.4430963397026062, 0.36364245414733887, 0.357366681098938, 0.4252263307571411, 0.4587792158126831, 0.49115538597106934, 0.36797642707824707, 0.2136552333831787, 0.3269249200820923, 0.6001182198524475]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.921900749206543})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5710737705230713})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4617178738117218})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4973987340927124})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4490979313850403})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4555947184562683})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4713614881038666})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.47405165433883667})
store['active_learning_steps'][28]['training']['best_epoch']=5
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.948, 'crossentropy': 0.3875071533203125}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7640262842178345})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.46138858795166016})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.38047826290130615})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3500140607357025})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3356689512729645})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.32424575090408325})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.31833457946777344})
store['active_learning_steps'][28]['eval_training']['best_epoch']=7
store['active_learning_steps'][28]['acquisition']={'indices': [57921, 50433, 18195, 1944, 8307, 31072, 59522, 17952, 3010, 16638], 'labels': [-1, 4, -1, -1, -1, -1, -1, -1, 7, -1], 'scores': [0.5196071863174438, 0.7021671533584595, 0.3278566598892212, 0.5297276377677917, 0.36308491230010986, 0.2516324520111084, 0.3865514397621155, 0.5386338829994202, 0.4835594892501831, 0.46133124828338623]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.0317131280899048})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5067518353462219})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4750811457633972})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.411257803440094})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.45762935280799866})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.44875770807266235})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.41775381565093994})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.956, 'crossentropy': 0.347407470703125}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7349438667297363})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.49923670291900635})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3931773602962494})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.35705435276031494})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.3550480604171753})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3503745496273041})
store['active_learning_steps'][29]['eval_training']['best_epoch']=6
store['active_learning_steps'][29]['acquisition']={'indices': [14866, 3062, 14266, 52573, 59671, 58884, 4968, 16340, 36282, 37062], 'labels': [-1, -1, 3, -1, -1, -1, -1, -1, 9, 9], 'scores': [0.2919667959213257, 0.43960320949554443, 0.5914921164512634, 0.3538992404937744, 0.3978671431541443, 0.3763936758041382, 0.31952357292175293, 0.4684814214706421, 0.5402041673660278, 0.4938703775405884]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9128549695014954})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4947540760040283})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.39888375997543335})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4701395630836487})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4134635925292969})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4407528042793274})
store['active_learning_steps'][30]['training']['best_epoch']=3
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9472, 'crossentropy': 0.3935404296875}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.754015326499939})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5316410064697266})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4311160743236542})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3875269591808319})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.411113977432251})
store['active_learning_steps'][30]['eval_training']['best_epoch']=4
store['active_learning_steps'][30]['acquisition']={'indices': [28376, 38613, 22278, 10412, 18598, 8459, 42047, 55285, 7767, 25897], 'labels': [5, 8, -1, 5, 9, 5, 5, -1, 3, -1], 'scores': [0.37139302492141724, 0.3680707812309265, 0.2134995460510254, 0.5360890626907349, 0.3891158103942871, 0.5564757585525513, 0.5309892892837524, 0.260888934135437, 0.41086435317993164, 0.2894953489303589]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 1.0727849006652832})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.48689842224121094})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.40424972772598267})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3933890461921692})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4153977036476135})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4178812503814697})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3998182415962219})
store['active_learning_steps'][31]['training']['best_epoch']=4
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9527, 'crossentropy': 0.363806591796875}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7475643157958984})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5114309787750244})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4029592275619507})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.38384872674942017})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.34419751167297363})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3267391324043274})
store['active_learning_steps'][31]['eval_training']['best_epoch']=6
store['active_learning_steps'][31]['acquisition']={'indices': [41223, 29903, 46437, 30462, 37906, 491, 11358, 14178, 35362, 48355], 'labels': [-1, 0, -1, -1, 9, -1, -1, -1, -1, -1], 'scores': [0.4210931062698364, 0.5234845876693726, 0.3393789529800415, 0.4590902328491211, 0.4114696979522705, 0.4203604459762573, 0.36799442768096924, 0.33532118797302246, 0.29170411825180054, 0.4109154939651489]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9218735694885254})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4886007308959961})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.379201203584671})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.41491425037384033})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.38870495557785034})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3964388370513916})
store['active_learning_steps'][32]['training']['best_epoch']=3
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9528, 'crossentropy': 0.3537190185546875}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7359098196029663})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4596116840839386})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4182206392288208})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3933415114879608})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3496363162994385})
store['active_learning_steps'][32]['eval_training']['best_epoch']=5
store['active_learning_steps'][32]['acquisition']={'indices': [5194, 23091, 49957, 59597, 47951, 43112, 31738, 13003, 14765, 38626], 'labels': [0, -1, 5, -1, 5, -1, 8, -1, 3, 5], 'scores': [0.46109992265701294, 0.35269564390182495, 0.4116172790527344, 0.30072522163391113, 0.377902626991272, 0.4254077672958374, 0.4158684015274048, 0.33196091651916504, 0.4312841296195984, 0.3188321590423584]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.0077202320098877})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5297431945800781})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.488348126411438})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4463438391685486})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4098273515701294})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4256790280342102})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.404448539018631})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3988839387893677})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4724007546901703})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.42484891414642334})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5101439952850342})
store['active_learning_steps'][33]['training']['best_epoch']=8
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9592, 'crossentropy': 0.35328623046875}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7226591110229492})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4256640374660492})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.35560959577560425})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3423909544944763})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3163614869117737})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.31747889518737793})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3015044927597046})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.30336225032806396})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3211536407470703})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.2942717969417572})
store['active_learning_steps'][33]['eval_training']['best_epoch']=10
store['active_learning_steps'][33]['acquisition']={'indices': [8783, 10226, 21990, 55265, 15280, 46328, 9372, 20322, 37281, 52392], 'labels': [7, -1, 1, -1, -1, -1, 9, 1, -1, 1], 'scores': [0.4718286693096161, 0.559337854385376, 0.6270002722740173, 0.43038809299468994, 0.5262078046798706, 0.381705641746521, 0.47786998748779297, 0.575629472732544, 0.5300686359405518, 0.6508117318153381]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.074091911315918})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.48135125637054443})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.43072324991226196})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3901550769805908})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4348500669002533})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.41795337200164795})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4461609125137329})
store['active_learning_steps'][34]['training']['best_epoch']=4
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.959, 'crossentropy': 0.3429543212890625}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7396795749664307})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.49375712871551514})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.39294570684432983})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3520991802215576})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3320196866989136})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.33840787410736084})
store['active_learning_steps'][34]['eval_training']['best_epoch']=5
store['active_learning_steps'][34]['acquisition']={'indices': [45088, 23788, 30176, 7368, 50431, 6002, 26214, 16722, 56138, 14462], 'labels': [-1, 1, 1, 5, 3, 1, 9, 1, 1, -1], 'scores': [0.3919041156768799, 0.4193185567855835, 0.2734224200248718, 0.5842748880386353, 0.48315346240997314, 0.5438270568847656, 0.3355957269668579, 0.46294957399368286, 0.5025678873062134, 0.28738778829574585]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.0312080383300781})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5465357303619385})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4370303153991699})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.40882349014282227})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4367097020149231})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4013277292251587})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4879623055458069})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.44439440965652466})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.40774965286254883})
store['active_learning_steps'][35]['training']['best_epoch']=6
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9566, 'crossentropy': 0.34501962890625}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.751825213432312})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.44424307346343994})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.37387096881866455})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.34636610746383667})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3419802188873291})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.31257128715515137})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3222973942756653})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.30691850185394287})
store['active_learning_steps'][35]['eval_training']['best_epoch']=8
store['active_learning_steps'][35]['acquisition']={'indices': [16912, 19824, 59875, 16690, 49438, 17742, 253, 32747, 14469, 22051], 'labels': [-1, 9, -1, -1, 8, -1, -1, 8, 4, 4], 'scores': [0.40594255924224854, 0.7273344397544861, 0.232183575630188, 0.5415594577789307, 0.47917211055755615, 0.4483180046081543, 0.46590662002563477, 0.6681694984436035, 0.47107982635498047, 0.2979939877986908]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.9816416501998901})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.545455276966095})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3817497193813324})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3817248046398163})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.36038872599601746})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.38317736983299255})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.40648674964904785})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3812128007411957})
store['active_learning_steps'][36]['training']['best_epoch']=5
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9579, 'crossentropy': 0.3232685302734375}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7851226925849915})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.46635815501213074})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.36131584644317627})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.35359135270118713})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.31431257724761963})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3243212103843689})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3077162504196167})
store['active_learning_steps'][36]['eval_training']['best_epoch']=7
store['active_learning_steps'][36]['acquisition']={'indices': [12514, 16565, 29085, 20869, 1083, 19549, 36884, 32843, 59718, 38912], 'labels': [2, -1, -1, 3, -1, 3, 2, -1, 8, -1], 'scores': [0.5408775806427002, 0.2749530076980591, 0.29698646068573, 0.5346882343292236, 0.34753739833831787, 0.3809523582458496, 0.6560460925102234, 0.30367112159729004, 0.48260825872421265, 0.5982608795166016]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.032753586769104})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.49945932626724243})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3888319730758667})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.42683660984039307})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3996758460998535})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.42171841859817505})
store['active_learning_steps'][37]['training']['best_epoch']=3
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9567, 'crossentropy': 0.3555579345703125}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7953011989593506})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5132416486740112})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4731714427471161})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4509735703468323})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.390587717294693})
store['active_learning_steps'][37]['eval_training']['best_epoch']=5
store['active_learning_steps'][37]['acquisition']={'indices': [50348, 58720, 42513, 24940, 11357, 5536, 49392, 55582, 57080, 23490], 'labels': [2, -1, -1, 0, -1, 8, -1, -1, -1, 3], 'scores': [0.41397523880004883, 0.43931663036346436, 0.3242419958114624, 0.4052256941795349, 0.46018922328948975, 0.44292956590652466, 0.3169819116592407, 0.41545259952545166, 0.41740846633911133, 0.5039299726486206]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9206222295761108})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5095112323760986})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4013856053352356})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3917156457901001})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.38148045539855957})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3959006071090698})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.40307796001434326})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3859260082244873})
store['active_learning_steps'][38]['training']['best_epoch']=5
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9579, 'crossentropy': 0.3386990966796875}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7783749103546143})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5019849538803101})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.37089282274246216})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.3481762409210205})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.31288379430770874})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3150104284286499})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.32196491956710815})
store['active_learning_steps'][38]['eval_training']['best_epoch']=5
store['active_learning_steps'][38]['acquisition']={'indices': [29956, 33812, 52613, 56580, 56740, 57718, 630, 56152, 31281, 24630], 'labels': [-1, 6, -1, -1, -1, 7, 6, 9, -1, 5], 'scores': [0.4996933937072754, 0.7931864261627197, 0.40493786334991455, 0.43029093742370605, 0.45146775245666504, 0.5809050798416138, 0.44398725032806396, 0.45263147354125977, 0.3566802740097046, 0.39871007204055786]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.0676500797271729})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.49447935819625854})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3541456460952759})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35981541872024536})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.36458268761634827})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.36184757947921753})
store['active_learning_steps'][39]['training']['best_epoch']=3
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9556, 'crossentropy': 0.337741064453125}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8108397126197815})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.515405535697937})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.46759581565856934})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.37252408266067505})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3899777829647064})
store['active_learning_steps'][39]['eval_training']['best_epoch']=4
store['active_learning_steps'][39]['acquisition']={'indices': [11949, 8780, 6466, 29279, 36908, 36268, 14428, 19702, 40169, 7438], 'labels': [-1, 8, 2, -1, 1, 5, 5, 5, 4, 7], 'scores': [0.30181193351745605, 0.3694286346435547, 0.4175192713737488, 0.19714760780334473, 0.2692962884902954, 0.4367847442626953, 0.32987111806869507, 0.3298588991165161, 0.3621569871902466, 0.43280649185180664]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.0769469738006592})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4835142493247986})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4093870520591736})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3528480529785156})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.37660813331604004})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4184260964393616})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3736385405063629})
store['active_learning_steps'][40]['training']['best_epoch']=4
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9592, 'crossentropy': 0.324410888671875}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7750288844108582})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.436307430267334})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3792566955089569})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3267993927001953})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3803651034832001})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.301940381526947})
store['active_learning_steps'][40]['eval_training']['best_epoch']=6
store['active_learning_steps'][40]['acquisition']={'indices': [13192, 10886, 22364, 45600, 37468, 2748, 39299, 12774, 8137, 41022], 'labels': [7, 1, 0, -1, 3, 2, 2, 7, 7, -1], 'scores': [0.46779757738113403, 0.3728911280632019, 0.4391833543777466, 0.237967848777771, 0.2921258807182312, 0.44782155752182007, 0.5066643953323364, 0.34925514459609985, 0.22381609678268433, 0.2926548719406128]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.1693315505981445})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6228960156440735})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4207736551761627})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.41158539056777954})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.39578789472579956})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4202146530151367})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4018254280090332})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4284785985946655})
store['active_learning_steps'][41]['training']['best_epoch']=5
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9587, 'crossentropy': 0.33227509765625}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7993248701095581})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.46526139974594116})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.37971293926239014})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3561636805534363})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3550233840942383})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2948545813560486})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.31877946853637695})
store['active_learning_steps'][41]['eval_training']['best_epoch']=6
store['active_learning_steps'][41]['acquisition']={'indices': [57450, 32341, 31307, 36392, 37078, 59548, 24272, 22607, 26564, 38912], 'labels': [8, -1, 1, 9, 8, -1, 4, 4, -1, -1], 'scores': [0.512915849685669, 0.35288357734680176, 0.3708761930465698, 0.4081617593765259, 0.6064776182174683, 0.4391193389892578, 0.4120780825614929, 0.5055275559425354, 0.42443788051605225, 0.6278332471847534]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.9590165019035339})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4685962200164795})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.37408247590065})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.356650173664093})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.344397634267807})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3858950436115265})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.39755937457084656})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4183022081851959})
store['active_learning_steps'][42]['training']['best_epoch']=5
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9627, 'crossentropy': 0.302958544921875}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7815395593643188})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4287078380584717})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.36314988136291504})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.33739930391311646})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.33234572410583496})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.329990029335022})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3246276378631592})
store['active_learning_steps'][42]['eval_training']['best_epoch']=7
store['active_learning_steps'][42]['acquisition']={'indices': [3726, 58752, 48330, 49740, 31887, 4112, 14572, 32670, 15823, 31664], 'labels': [-1, -1, 9, 9, -1, -1, 4, 6, -1, 3], 'scores': [0.3346899747848511, 0.22165310382843018, 0.47276628017425537, 0.252845823764801, 0.4663735628128052, 0.31385213136672974, 0.316305011510849, 0.4487481713294983, 0.33538174629211426, 0.4086897373199463]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.088253378868103})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5116875171661377})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3860059380531311})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.37191063165664673})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4105084538459778})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3918115496635437})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.41265201568603516})
store['active_learning_steps'][43]['training']['best_epoch']=4
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9626, 'crossentropy': 0.3199207763671875}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8083783388137817})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.48829755187034607})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4389866590499878})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3999236822128296})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3536904454231262})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.39891156554222107})
store['active_learning_steps'][43]['eval_training']['best_epoch']=5
store['active_learning_steps'][43]['acquisition']={'indices': [12018, 5466, 6604, 48160, 120, 19327, 18682, 1642, 54858, 18525], 'labels': [7, -1, 8, -1, -1, -1, -1, 6, 3, 6], 'scores': [0.3990182876586914, 0.2803839445114136, 0.5624982714653015, 0.4980643391609192, 0.4133700132369995, 0.3475126028060913, 0.2885476350784302, 0.6260491013526917, 0.438632607460022, 0.43923741579055786]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.000220537185669})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4887987971305847})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3706256151199341})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.41562482714653015})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.43868327140808105})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4222886860370636})
store['active_learning_steps'][44]['training']['best_epoch']=3
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.9546, 'crossentropy': 0.3363791015625}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7982600927352905})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5310516953468323})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4264216423034668})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4178375005722046})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3547360301017761})
store['active_learning_steps'][44]['eval_training']['best_epoch']=5
store['active_learning_steps'][44]['acquisition']={'indices': [37138, 403, 48735, 6574, 57357, 17831, 52931, 47140, 25801, 3181], 'labels': [-1, -1, -1, -1, -1, -1, 3, 3, -1, -1], 'scores': [0.4012312889099121, 0.397192120552063, 0.3470451831817627, 0.41351956129074097, 0.21195203065872192, 0.3504953384399414, 0.3774265646934509, 0.5025884509086609, 0.31932568550109863, 0.27611398696899414]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.0223333835601807})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4884270131587982})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34779268503189087})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3045005798339844})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3323838710784912})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.35850417613983154})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.36205923557281494})
store['active_learning_steps'][45]['training']['best_epoch']=4
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.9635, 'crossentropy': 0.295411083984375}
store['active_learning_steps'][45]['eval_training']={}
store['active_learning_steps'][45]['eval_training']['epochs']=[]
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7228289842605591})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4381176233291626})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.354520320892334})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3171370327472687})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3674234449863434})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3274328410625458})
store['active_learning_steps'][45]['eval_training']['best_epoch']=4
store['active_learning_steps'][45]['acquisition']={'indices': [24616, 20569, 31313, 19607, 36262, 46533, 1596, 44887, 46547, 51242], 'labels': [-1, 5, 8, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.32621681690216064, 0.504603922367096, 0.43505018949508667, 0.38378727436065674, 0.4383314847946167, 0.2655740976333618, 0.5874693393707275, 0.4296001195907593, 0.45499372482299805, 0.32925617694854736]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.082961082458496})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.45355790853500366})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3820323944091797})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34597745537757874})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3891119360923767})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34205085039138794})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.38562363386154175})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.36389386653900146})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.38342368602752686})
store['active_learning_steps'][46]['training']['best_epoch']=6
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.9663, 'crossentropy': 0.2781787841796875}
store['active_learning_steps'][46]['eval_training']={}
store['active_learning_steps'][46]['eval_training']['epochs']=[]
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7839158177375793})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4634968638420105})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3497874140739441})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3398768901824951})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.33430400490760803})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.31492769718170166})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.29402852058410645})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2875847816467285})
store['active_learning_steps'][46]['eval_training']['best_epoch']=8
store['active_learning_steps'][46]['acquisition']={'indices': [21222, 34847, 37750, 40688, 6834, 58445, 49515, 24780, 27971, 42703], 'labels': [-1, 0, 5, -1, -1, -1, 2, -1, -1, 0], 'scores': [0.4251912832260132, 0.5625771284103394, 0.5136248469352722, 0.5730119943618774, 0.5749744176864624, 0.5476549863815308, 0.5178546905517578, 0.382961630821228, 0.3877592086791992, 0.49330198764801025]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.0498590469360352})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.48832476139068604})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3596971035003662})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3572286367416382})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3707472085952759})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3831682801246643})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.38333070278167725})
store['active_learning_steps'][47]['training']['best_epoch']=4
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.9624, 'crossentropy': 0.3020810791015625}
store['active_learning_steps'][47]['eval_training']={}
store['active_learning_steps'][47]['eval_training']['epochs']=[]
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8538264632225037})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.52435702085495})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4483697712421417})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3527888059616089})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3518211841583252})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.36345410346984863})
store['active_learning_steps'][47]['eval_training']['best_epoch']=5
store['active_learning_steps'][47]['acquisition']={'indices': [15099, 46601, 16152, 42866, 9608, 31571, 22083, 38587, 46274, 40890], 'labels': [-1, -1, -1, 2, 8, -1, 2, -1, 7, -1], 'scores': [0.37843167781829834, 0.43520987033843994, 0.3792504072189331, 0.5999824404716492, 0.522127091884613, 0.3397848606109619, 0.5043649673461914, 0.3830450773239136, 0.4963167905807495, 0.46615493297576904]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.1337608098983765})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.47282522916793823})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.39494746923446655})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.36169204115867615})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.360247403383255})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.39977332949638367})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3629198670387268})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3697441816329956})
store['active_learning_steps'][48]['training']['best_epoch']=5
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.9636, 'crossentropy': 0.2855800048828125}
store['active_learning_steps'][48]['eval_training']={}
store['active_learning_steps'][48]['eval_training']['epochs']=[]
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8037657737731934})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4596151113510132})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.35712292790412903})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3583136200904846})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.31302958726882935})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.31287652254104614})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2797926366329193})
store['active_learning_steps'][48]['eval_training']['best_epoch']=7
store['active_learning_steps'][48]['acquisition']={'indices': [11162, 47365, 52140, 788, 3672, 41639, 25096, 21136, 25986, 13969], 'labels': [0, 4, 4, 9, -1, 3, 5, 2, 8, 3], 'scores': [0.5569707155227661, 0.3945322036743164, 0.4714090824127197, 0.4449845552444458, 0.2538414001464844, 0.4862402677536011, 0.5038799047470093, 0.5068420767784119, 0.44404715299606323, 0.40054434537887573]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.1001222133636475})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5271198749542236})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.37943562865257263})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3392830491065979})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31996792554855347})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3473837971687317})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3546324372291565})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3496563732624054})
store['active_learning_steps'][49]['training']['best_epoch']=5
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.9658, 'crossentropy': 0.2814766357421875}
store['active_learning_steps'][49]['eval_training']={}
store['active_learning_steps'][49]['eval_training']['epochs']=[]
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8699832558631897})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4674032926559448})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4030442535877228})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.35494285821914673})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.32339411973953247})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.32293713092803955})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.32937103509902954})
store['active_learning_steps'][49]['eval_training']['best_epoch']=6
store['active_learning_steps'][49]['acquisition']={'indices': [42817, 36408, 13025, 44898, 26733, 39656, 11600, 33185, 49297, 9431], 'labels': [-1, 1, 1, 2, 2, 0, -1, -1, -1, 4], 'scores': [0.34355664253234863, 0.44865483045578003, 0.31869053840637207, 0.4584314823150635, 0.4793841242790222, 0.34428298473358154, 0.4066047668457031, 0.3310850262641907, 0.3053678274154663, 0.36810797452926636]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.0894758701324463})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5104913711547852})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.395174503326416})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3287661075592041})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3216610848903656})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.37388357520103455})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.38274288177490234})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3759693205356598})
store['active_learning_steps'][50]['training']['best_epoch']=5
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.9589, 'crossentropy': 0.3049743408203125}
store['active_learning_steps'][50]['eval_training']={}
store['active_learning_steps'][50]['eval_training']['epochs']=[]
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.948268473148346})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5102754831314087})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4181020259857178})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.360591322183609})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.33823055028915405})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.32075244188308716})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.34009820222854614})
store['active_learning_steps'][50]['eval_training']['best_epoch']=6
store['active_learning_steps'][50]['acquisition']={'indices': [46151, 43209, 57246, 40046, 35478, 9583, 32776, 23028, 14354, 30493], 'labels': [-1, -1, -1, 7, -1, -1, 4, 2, -1, 1], 'scores': [0.36943066120147705, 0.42718303203582764, 0.48783767223358154, 0.5228725075721741, 0.3432213068008423, 0.36279523372650146, 0.6022430062294006, 0.4662182629108429, 0.3878408670425415, 0.42118048667907715]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.1169236898422241})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4948723018169403})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4128350019454956})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.36528199911117554})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3341325521469116})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.35444462299346924})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.36419999599456787})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3661106824874878})
store['active_learning_steps'][51]['training']['best_epoch']=5
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.962, 'crossentropy': 0.310237451171875}
store['active_learning_steps'][51]['eval_training']={}
store['active_learning_steps'][51]['eval_training']['epochs']=[]
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8334182500839233})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.47997570037841797})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.379518985748291})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30237895250320435})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3140775263309479})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3071492314338684})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3175238370895386})
store['active_learning_steps'][51]['eval_training']['best_epoch']=4
store['active_learning_steps'][51]['acquisition']={'indices': [59938, 35732, 18754, 5214, 27521, 1313, 19328, 59653, 26622, 46958], 'labels': [-1, 9, 7, -1, -1, -1, 5, 0, 6, 9], 'scores': [0.3157923221588135, 0.3377988338470459, 0.457314670085907, 0.2332521677017212, 0.4547918438911438, 0.340060830116272, 0.4192490577697754, 0.45850884914398193, 0.399726927280426, 0.3876945972442627]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.0305980443954468})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5532768368721008})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.41631969809532166})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3769901990890503})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3153247833251953})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3384496867656708})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3172570466995239})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3644517660140991})
store['active_learning_steps'][52]['training']['best_epoch']=5
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.967, 'crossentropy': 0.2792276611328125}
store['active_learning_steps'][52]['eval_training']={}
store['active_learning_steps'][52]['eval_training']['epochs']=[]
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.850373387336731})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.49116405844688416})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3866503834724426})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34802427887916565})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.32511427998542786})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2964560389518738})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31237149238586426})
store['active_learning_steps'][52]['eval_training']['best_epoch']=6
store['active_learning_steps'][52]['acquisition']={'indices': [11742, 54520, 2335, 17540, 19868, 36744, 50827, 14580, 49082, 14607], 'labels': [0, 9, -1, 1, 5, 1, 1, 9, 3, 9], 'scores': [0.264093816280365, 0.38954973220825195, 0.33140599727630615, 0.4524783492088318, 0.5349504351615906, 0.5621216297149658, 0.3017423748970032, 0.36620843410491943, 0.5284640192985535, 0.2553141713142395]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.1848762035369873})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5757652521133423})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3847930431365967})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3289054036140442})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.36322298645973206})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.37971436977386475})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.37475526332855225})
store['active_learning_steps'][53]['training']['best_epoch']=4
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.9571, 'crossentropy': 0.320343115234375}
store['active_learning_steps'][53]['eval_training']={}
store['active_learning_steps'][53]['eval_training']['epochs']=[]
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9382007122039795})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5265549421310425})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4360867142677307})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4362010657787323})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4278147220611572})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.35950934886932373})
store['active_learning_steps'][53]['eval_training']['best_epoch']=6
store['active_learning_steps'][53]['acquisition']={'indices': [49977, 137, 50727, 3680, 36942, 29018, 53268, 6595, 58058, 31871], 'labels': [-1, 8, -1, -1, 2, -1, -1, -1, 8, -1], 'scores': [0.31556451320648193, 0.31209689378738403, 0.31318509578704834, 0.3056049346923828, 0.37009716033935547, 0.3614133596420288, 0.23420560359954834, 0.34072577953338623, 0.33402252197265625, 0.27398014068603516]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.0368454456329346})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5982723832130432})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3823789954185486})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3280197083950043})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.34516555070877075})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2756342589855194})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32648640871047974})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3395496606826782})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33548226952552795})
store['active_learning_steps'][54]['training']['best_epoch']=6
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.9657, 'crossentropy': 0.2692776611328125}
store['active_learning_steps'][54]['eval_training']={}
store['active_learning_steps'][54]['eval_training']['epochs']=[]
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8714659810066223})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5159726142883301})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.36508145928382874})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35964101552963257})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.30710524320602417})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3062187433242798})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2871948480606079})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.27977120876312256})
store['active_learning_steps'][54]['eval_training']['best_epoch']=8
store['active_learning_steps'][54]['acquisition']={'indices': [47172, 24250, 32918, 50486, 41426, 890, 42392, 57683, 49400, 36818], 'labels': [-1, 5, 2, -1, 4, -1, 5, 9, -1, 7], 'scores': [0.3470633029937744, 0.34736520051956177, 0.5350364446640015, 0.35713911056518555, 0.5834932327270508, 0.3773757219314575, 0.31026017665863037, 0.44168442487716675, 0.4644712209701538, 0.5173162221908569]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.0584430694580078})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.606184720993042})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.37215492129325867})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3937171995639801})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3047173023223877})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.35587021708488464})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3253409266471863})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3146930932998657})
store['active_learning_steps'][55]['training']['best_epoch']=5
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.9615, 'crossentropy': 0.3067973876953125}
store['active_learning_steps'][55]['eval_training']={}
store['active_learning_steps'][55]['eval_training']['epochs']=[]
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.840658962726593})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5159313082695007})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.41159486770629883})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3711833655834198})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3207736015319824})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.32941651344299316})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3338121175765991})
store['active_learning_steps'][55]['eval_training']['best_epoch']=5
store['active_learning_steps'][55]['acquisition']={'indices': [22050, 13276, 48638, 59145, 14105, 55102, 20982, 53872, 34771, 37680], 'labels': [-1, 5, 0, -1, -1, 9, -1, 8, 0, -1], 'scores': [0.2699108123779297, 0.445362389087677, 0.5579318404197693, 0.2716885805130005, 0.24893701076507568, 0.32085302472114563, 0.3168832063674927, 0.5140954852104187, 0.486062228679657, 0.30641233921051025]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.113560676574707})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.48751553893089294})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3772728443145752})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3159639239311218})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3344807028770447})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.31482312083244324})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31396639347076416})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.34591421484947205})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35645413398742676})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3549126386642456})
store['active_learning_steps'][56]['training']['best_epoch']=7
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.9689, 'crossentropy': 0.2698252685546875}
store['active_learning_steps'][56]['eval_training']={}
store['active_learning_steps'][56]['eval_training']['epochs']=[]
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.024269461631775})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5478590130805969})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.447589635848999})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.33181482553482056})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3140713572502136})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3041927218437195})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.28389304876327515})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2715509235858917})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.27144619822502136})
store['active_learning_steps'][56]['eval_training']['best_epoch']=9
store['active_learning_steps'][56]['acquisition']={'indices': [5285, 20095, 56291, 45867, 4955, 17296, 581, 11852, 57336, 51952], 'labels': [-1, -1, -1, -1, 2, 9, -1, 4, 3, -1], 'scores': [0.34285783767700195, 0.35437488555908203, 0.3288062810897827, 0.3918510675430298, 0.5381084680557251, 0.5811110734939575, 0.2558490037918091, 0.4542819857597351, 0.4864049553871155, 0.5098487734794617]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.232439637184143})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5800713300704956})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.41336846351623535})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3632725179195404})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31840255856513977})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34941112995147705})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32392752170562744})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3437071740627289})
store['active_learning_steps'][57]['training']['best_epoch']=5
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.9666, 'crossentropy': 0.300215673828125}
store['active_learning_steps'][57]['eval_training']={}
store['active_learning_steps'][57]['eval_training']['epochs']=[]
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8113120198249817})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5070778131484985})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.39857935905456543})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3513745069503784})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3437870144844055})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3346759080886841})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.33016806840896606})
store['active_learning_steps'][57]['eval_training']['best_epoch']=7
store['active_learning_steps'][57]['acquisition']={'indices': [1297, 40199, 49362, 28338, 619, 27420, 21218, 2424, 43176, 23185], 'labels': [-1, -1, -1, -1, -1, -1, 9, -1, 2, -1], 'scores': [0.35527414083480835, 0.3061225414276123, 0.2410295605659485, 0.33240342140197754, 0.36496418714523315, 0.4286154508590698, 0.3954847455024719, 0.22188341617584229, 0.534791886806488, 0.454193115234375]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.0505300760269165})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.529854953289032})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4065784215927124})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3542276620864868})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.2967959940433502})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30408281087875366})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3093961179256439})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.33359360694885254})
store['active_learning_steps'][58]['training']['best_epoch']=5
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.965, 'crossentropy': 0.269455224609375}
store['active_learning_steps'][58]['eval_training']={}
store['active_learning_steps'][58]['eval_training']['epochs']=[]
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.9511963725090027})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4935232698917389})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.41093170642852783})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.33558136224746704})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.33426690101623535})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.289884477853775})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3159905672073364})
store['active_learning_steps'][58]['eval_training']['best_epoch']=6
store['active_learning_steps'][58]['acquisition']={'indices': [24128, 45819, 32914, 7125, 50037, 4343, 50698, 46432, 42646, 6879], 'labels': [-1, -1, -1, 7, 7, -1, 9, 6, -1, -1], 'scores': [0.2998000383377075, 0.30400848388671875, 0.2947911024093628, 0.5096386671066284, 0.3132748007774353, 0.23120319843292236, 0.4565911293029785, 0.5696588754653931, 0.2991774082183838, 0.27349090576171875]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.1904762983322144})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5617862939834595})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.39975130558013916})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3600570261478424})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31740814447402954})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30732423067092896})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32959142327308655})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3074403405189514})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3123800754547119})
store['active_learning_steps'][59]['training']['best_epoch']=6
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.969, 'crossentropy': 0.279885546875}
store['active_learning_steps'][59]['eval_training']={}
store['active_learning_steps'][59]['eval_training']['epochs']=[]
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8635079860687256})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5382841229438782})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.39418938755989075})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3167009651660919})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30233532190322876})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30100834369659424})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2915380597114563})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.26357054710388184})
store['active_learning_steps'][59]['eval_training']['best_epoch']=8
store['active_learning_steps'][59]['acquisition']={'indices': [48177, 28380, 56235, 59335, 18473, 14940, 31557, 51282, 9767, 12127], 'labels': [-1, -1, -1, 4, 4, 6, -1, -1, -1, 9], 'scores': [0.3319878578186035, 0.38538074493408203, 0.37849628925323486, 0.5300335884094238, 0.4891308546066284, 0.4975002408027649, 0.4775353670120239, 0.3356482982635498, 0.38289427757263184, 0.3460085391998291]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.2270379066467285})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5897156000137329})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4022197127342224})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3566873371601105})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3179302215576172})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3185023069381714})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2705150842666626})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31302252411842346})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3106122314929962})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3049272894859314})
store['active_learning_steps'][60]['training']['best_epoch']=7
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.9715, 'crossentropy': 0.27151455078125}
store['active_learning_steps'][60]['eval_training']={}
store['active_learning_steps'][60]['eval_training']['epochs']=[]
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8753347396850586})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4644400179386139})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3567543923854828})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.31512895226478577})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3327852487564087})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3183743357658386})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2655910551548004})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.31335121393203735})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2943653464317322})
store['active_learning_steps'][60]['eval_training']['best_epoch']=7
store['active_learning_steps'][60]['acquisition']={'indices': [22898, 52223, 20965, 40188, 11682, 15163, 15666, 5398, 40962, 2291], 'labels': [-1, -1, -1, 0, 9, -1, -1, -1, -1, -1], 'scores': [0.3925286531448364, 0.3785668611526489, 0.40374821424484253, 0.4342989921569824, 0.3149527907371521, 0.2888728976249695, 0.34649962186813354, 0.24000799655914307, 0.4184432029724121, 0.35153913497924805]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.1022615432739258})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.49305373430252075})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3583926558494568})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32955604791641235})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3227519989013672})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2789531648159027})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2962685227394104})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2791582942008972})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3244500458240509})
store['active_learning_steps'][61]['training']['best_epoch']=6
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.9673, 'crossentropy': 0.2740794189453125}
store['active_learning_steps'][61]['eval_training']={}
store['active_learning_steps'][61]['eval_training']['epochs']=[]
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8373129963874817})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.49983564019203186})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3458034098148346})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3475075960159302})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30033519864082336})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2753365635871887})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2588259279727936})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.28008291125297546})
store['active_learning_steps'][61]['eval_training']['best_epoch']=7
store['active_learning_steps'][61]['acquisition']={'indices': [11410, 21601, 31289, 21148, 32880, 39474, 20363, 5758, 45470, 48084], 'labels': [-1, 1, 6, 7, 0, 0, 8, 2, 5, -1], 'scores': [0.29106712341308594, 0.4849885106086731, 0.3628932237625122, 0.21486616134643555, 0.5429022312164307, 0.37161684036254883, 0.2991253733634949, 0.43757474422454834, 0.20589670538902283, 0.27232372760772705]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.0451321601867676})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5384194850921631})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3776261806488037})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.33887118101119995})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2822114825248718})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.29971322417259216})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2785317003726959})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29201561212539673})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29470980167388916})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3252878785133362})
store['active_learning_steps'][62]['training']['best_epoch']=7
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.9705, 'crossentropy': 0.249698876953125}
store['active_learning_steps'][62]['eval_training']={}
store['active_learning_steps'][62]['eval_training']['epochs']=[]
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8518570065498352})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5583344101905823})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4025910496711731})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.33240169286727905})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.28685230016708374})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2522425651550293})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.25757378339767456})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2632574737071991})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.25671324133872986})
store['active_learning_steps'][62]['eval_training']['best_epoch']=6
store['active_learning_steps'][62]['acquisition']={'indices': [10948, 46146, 14178, 29875, 20280, 39316, 19837, 33524, 725, 22561], 'labels': [-1, -1, -1, -1, 7, -1, -1, -1, -1, 6], 'scores': [0.3504599332809448, 0.37750566005706787, 0.3246349096298218, 0.5896008014678955, 0.5474851727485657, 0.3937201499938965, 0.4411109685897827, 0.3352828025817871, 0.39407622814178467, 0.5937466621398926]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.1971862316131592})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.6217963099479675})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3930429220199585})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35379135608673096})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30132490396499634})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2942037582397461})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2967004179954529})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31521284580230713})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28308480978012085})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27425646781921387})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34139910340309143})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30993497371673584})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3259909152984619})
store['active_learning_steps'][63]['training']['best_epoch']=10
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.9712, 'crossentropy': 0.2568302734375}
store['active_learning_steps'][63]['eval_training']={}
store['active_learning_steps'][63]['eval_training']['epochs']=[]
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.866063117980957})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.45495983958244324})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.33300381898880005})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.29352641105651855})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2858527898788452})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2608874440193176})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2669079303741455})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.25657063722610474})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.23489344120025635})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.26279687881469727})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.237773597240448})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.23661492764949799})
store['active_learning_steps'][63]['eval_training']['best_epoch']=9
store['active_learning_steps'][63]['acquisition']={'indices': [16320, 14446, 12088, 43648, 14282, 8256, 59139, 15741, 3843, 13085], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, 6], 'scores': [0.4302384853363037, 0.47096872329711914, 0.2997562885284424, 0.4378478527069092, 0.39157599210739136, 0.36827588081359863, 0.48160338401794434, 0.45909953117370605, 0.3815215826034546, 0.5505354404449463]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.1230418682098389})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.48394739627838135})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.38129913806915283})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3130227029323578})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2733411490917206})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3096146881580353})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.302398145198822})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3021430969238281})
store['active_learning_steps'][64]['training']['best_epoch']=5
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9663, 'crossentropy': 0.26834921875}
store['active_learning_steps'][64]['eval_training']={}
store['active_learning_steps'][64]['eval_training']['epochs']=[]
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.9246936440467834})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.522938072681427})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.41728371381759644})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32976043224334717})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3387278616428375})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30884963274002075})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.29314127564430237})
store['active_learning_steps'][64]['eval_training']['best_epoch']=7
store['active_learning_steps'][64]['acquisition']={'indices': [24740, 20350, 52462, 16698, 8090, 25411, 43728, 18324, 3136, 33494], 'labels': [-1, 8, 9, 5, -1, -1, -1, 0, 6, -1], 'scores': [0.43764758110046387, 0.28773045539855957, 0.4893501400947571, 0.3356630206108093, 0.3619469404220581, 0.37164831161499023, 0.2653038501739502, 0.5492826104164124, 0.4004957675933838, 0.38559043407440186]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.1175360679626465})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.49644047021865845})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3536790907382965})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.328471839427948})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2974320352077484})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3019781708717346})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3029628396034241})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28587111830711365})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2810449004173279})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3062518835067749})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2994230389595032})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.287422776222229})
store['active_learning_steps'][65]['training']['best_epoch']=9
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.9719, 'crossentropy': 0.247694189453125}
store['active_learning_steps'][65]['eval_training']={}
store['active_learning_steps'][65]['eval_training']['epochs']=[]
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.9046787023544312})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.49194830656051636})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.37388554215431213})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.326480507850647})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3109034597873688})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.29204273223876953})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2663459777832031})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.23826363682746887})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2567501962184906})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.22271868586540222})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.24538950622081757})
store['active_learning_steps'][65]['eval_training']['best_epoch']=10
store['active_learning_steps'][65]['acquisition']={'indices': [54482, 40334, 58668, 11374, 10530, 4944, 158, 47225, 34908, 26676], 'labels': [-1, 4, -1, -1, -1, -1, 7, 3, -1, -1], 'scores': [0.3841438293457031, 0.8335657119750977, 0.43431681394577026, 0.39463770389556885, 0.38586723804473877, 0.2586970329284668, 0.4261600971221924, 0.3603719472885132, 0.32080864906311035, 0.33291095495224]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9854599237442017})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5301371812820435})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4243251085281372})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3030281960964203})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3143911361694336})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2918647825717926})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29074838757514954})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3031526505947113})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3092408776283264})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29509493708610535})
store['active_learning_steps'][66]['training']['best_epoch']=7
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.9684, 'crossentropy': 0.25138642578125}
store['active_learning_steps'][66]['eval_training']={}
store['active_learning_steps'][66]['eval_training']['epochs']=[]
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.9334672689437866})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5220343470573425})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3856940269470215})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3523819148540497})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32140111923217773})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31478792428970337})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.29918956756591797})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2816295027732849})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2666679322719574})
store['active_learning_steps'][66]['eval_training']['best_epoch']=9
store['active_learning_steps'][66]['acquisition']={'indices': [16632, 21880, 31727, 12756, 51843, 59215, 2502, 55032, 12061, 45628], 'labels': [-1, 2, -1, -1, -1, -1, 7, -1, -1, -1], 'scores': [0.5165045261383057, 0.6425510048866272, 0.3922457695007324, 0.40284013748168945, 0.48753905296325684, 0.4202601909637451, 0.4204713702201843, 0.4180793762207031, 0.3604811429977417, 0.532538652420044]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.217153787612915})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.627830445766449})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.39562153816223145})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.35288721323013306})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3230622112751007})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3415968418121338})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31861889362335205})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3420075476169586})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.33139774203300476})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31943899393081665})
store['active_learning_steps'][67]['training']['best_epoch']=7
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9672, 'crossentropy': 0.27654560546875}
store['active_learning_steps'][67]['eval_training']={}
store['active_learning_steps'][67]['eval_training']['epochs']=[]
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8622388243675232})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.528151273727417})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.37704208493232727})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3252445161342621})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2960987389087677})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2878791391849518})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2778868079185486})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2835664451122284})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2798865735530853})
store['active_learning_steps'][67]['eval_training']['best_epoch']=7
store['active_learning_steps'][67]['acquisition']={'indices': [12751, 23212, 45666, 18690, 1887, 2546, 56276, 4848, 30755, 55738], 'labels': [-1, -1, 1, -1, -1, 4, -1, -1, -1, -1], 'scores': [0.37072014808654785, 0.39020490646362305, 0.4884743094444275, 0.3862977623939514, 0.40394502878189087, 0.31250208616256714, 0.3577761650085449, 0.4318963289260864, 0.41393017768859863, 0.3240821361541748]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.1377246379852295})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5721434354782104})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.364724338054657})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3224019408226013})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31218504905700684})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34127408266067505})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3124404549598694})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.31752532720565796})
store['active_learning_steps'][68]['training']['best_epoch']=5
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9677, 'crossentropy': 0.278212060546875}
store['active_learning_steps'][68]['eval_training']={}
store['active_learning_steps'][68]['eval_training']['epochs']=[]
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8415191769599915})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5202698111534119})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.43871402740478516})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3803443908691406})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3527366518974304})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3248916268348694})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.29245710372924805})
store['active_learning_steps'][68]['eval_training']['best_epoch']=7
store['active_learning_steps'][68]['acquisition']={'indices': [8135, 9176, 13079, 4276, 36365, 54168, 10889, 32190, 45571, 6608], 'labels': [-1, -1, -1, 3, -1, -1, -1, 7, -1, 4], 'scores': [0.37319302558898926, 0.2958124876022339, 0.3599759340286255, 0.2968318462371826, 0.4291466474533081, 0.1553741693496704, 0.3389056921005249, 0.2914011478424072, 0.22022056579589844, 0.350689172744751]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.1242493391036987})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5081812739372253})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.37933605909347534})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3485470712184906})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2736448645591736})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28020715713500977})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29460689425468445})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.26932811737060547})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2702450454235077})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.32398539781570435})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.33958888053894043})
store['active_learning_steps'][69]['training']['best_epoch']=8
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.972, 'crossentropy': 0.2547008544921875}
store['active_learning_steps'][69]['eval_training']={}
store['active_learning_steps'][69]['eval_training']['epochs']=[]
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8895241022109985})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4911617040634155})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3567795753479004})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31337177753448486})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2864965796470642})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.282109797000885})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.26504218578338623})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2596472203731537})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.24988332390785217})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2521471083164215})
store['active_learning_steps'][69]['eval_training']['best_epoch']=9
store['active_learning_steps'][69]['acquisition']={'indices': [19566, 32592, 12836, 3626, 31576, 33433, 35071, 28954, 740, 30838], 'labels': [-1, -1, 3, 3, 7, -1, -1, -1, 8, 9], 'scores': [0.48024433851242065, 0.4485588073730469, 0.42504191398620605, 0.3015958070755005, 0.5624480247497559, 0.39503777027130127, 0.4352996349334717, 0.38378965854644775, 0.5360773801803589, 0.4508014917373657]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.0692379474639893})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5700350999832153})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.32442253828048706})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2916829288005829})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2940062880516052})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3110690116882324})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2684880197048187})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2398160696029663})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2828761339187622})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30807027220726013})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.29562294483184814})
store['active_learning_steps'][70]['training']['best_epoch']=8
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.9748, 'crossentropy': 0.2337318359375}
store['active_learning_steps'][70]['eval_training']={}
store['active_learning_steps'][70]['eval_training']['epochs']=[]
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8467706441879272})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4628944396972656})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3671901226043701})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35245394706726074})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2809886336326599})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2664429247379303})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2528655230998993})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.267874151468277})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2431597113609314})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.23594805598258972})
store['active_learning_steps'][70]['eval_training']['best_epoch']=10
store['active_learning_steps'][70]['acquisition']={'indices': [4590, 991, 46728, 1164, 32867, 48804, 42560, 22064, 29656, 53121], 'labels': [5, -1, 4, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.6727686524391174, 0.3137780427932739, 0.5976331830024719, 0.389193058013916, 0.4435081481933594, 0.4383803606033325, 0.40860986709594727, 0.38935595750808716, 0.448868989944458, 0.24169480800628662]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.0568468570709229})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5574389100074768})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.37958627939224243})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32631176710128784})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29691576957702637})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28971171379089355})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2841384708881378})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.32067424058914185})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2781110405921936})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2633403539657593})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.300536572933197})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2582748830318451})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.31041961908340454})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.29311609268188477})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2814411520957947})
store['active_learning_steps'][71]['training']['best_epoch']=12
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9751, 'crossentropy': 0.2429276611328125}
store['active_learning_steps'][71]['eval_training']={}
store['active_learning_steps'][71]['eval_training']['epochs']=[]
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.0107122659683228})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5335354804992676})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3815045952796936})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3354823589324951})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2802705466747284})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2688714265823364})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.26368820667266846})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2477596253156662})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2405780851840973})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.24625572562217712})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2357933521270752})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.22599227726459503})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.21853792667388916})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.22747310996055603})
store['active_learning_steps'][71]['eval_training']['best_epoch']=13
store['active_learning_steps'][71]['acquisition']={'indices': [37360, 37202, 24660, 3357, 9928, 27429, 29193, 39419, 42212, 11294], 'labels': [2, -1, -1, -1, -1, 0, -1, 8, -1, -1], 'scores': [0.4819786250591278, 0.32713770866394043, 0.3308769464492798, 0.5514379739761353, 0.4100378155708313, 0.5573562383651733, 0.5159470438957214, 0.4083538055419922, 0.453880250453949, 0.3614999055862427]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 1.0826057195663452})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.47682374715805054})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.34782958030700684})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2970206141471863})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3141430616378784})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3029335141181946})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27725309133529663})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2854585647583008})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29115214943885803})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2715521454811096})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.29187434911727905})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.26984554529190063})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2938326597213745})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.31717002391815186})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2811158299446106})
store['active_learning_steps'][72]['training']['best_epoch']=12
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.9731, 'crossentropy': 0.2492846435546875}
store['active_learning_steps'][72]['eval_training']={}
store['active_learning_steps'][72]['eval_training']['epochs']=[]
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9148416519165039})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4902583956718445})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.39693593978881836})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32623282074928284})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3137379288673401})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2542225420475006})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2749718427658081})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2656627893447876})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.23484322428703308})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24354287981987})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24638691544532776})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.23383495211601257})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2415042519569397})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.22632113099098206})
store['active_learning_steps'][72]['eval_training']['best_epoch']=14
store['active_learning_steps'][72]['acquisition']={'indices': [38780, 21683, 8645, 34920, 7704, 15958, 55896, 30386, 54586, 43174], 'labels': [6, -1, -1, 9, 8, 2, 7, -1, 9, -1], 'scores': [0.5152732729911804, 0.42051172256469727, 0.46987080574035645, 0.585472047328949, 0.5323532223701477, 0.6045608222484589, 0.5259131193161011, 0.36962974071502686, 0.49390923976898193, 0.30826425552368164]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.1369924545288086})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5569387078285217})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3812713623046875})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30961889028549194})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31642717123031616})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2852556109428406})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30333447456359863})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2808059751987457})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29829898476600647})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29082536697387695})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.31244003772735596})
store['active_learning_steps'][73]['training']['best_epoch']=8
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9754, 'crossentropy': 0.2563195068359375}
store['active_learning_steps'][73]['eval_training']={}
store['active_learning_steps'][73]['eval_training']['epochs']=[]
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8933213949203491})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.520283579826355})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3847569227218628})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30056482553482056})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3159139156341553})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2668156921863556})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.25418245792388916})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.25946980714797974})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29571449756622314})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.23910167813301086})
store['active_learning_steps'][73]['eval_training']['best_epoch']=10
store['active_learning_steps'][73]['acquisition']={'indices': [52953, 6005, 55620, 58776, 50946, 20072, 32521, 7793, 11848, 49599], 'labels': [2, -1, 8, 8, 3, 3, -1, 8, 0, 9], 'scores': [0.6064784526824951, 0.3533604145050049, 0.5651860237121582, 0.4078713655471802, 0.5771466493606567, 0.5500830411911011, 0.4655003547668457, 0.5654764771461487, 0.4849472641944885, 0.4467403292655945]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.1540902853012085})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5206007957458496})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4014410376548767})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3196621537208557})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3102477192878723})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28890782594680786})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2920414209365845})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.293956995010376})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.26757073402404785})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29096370935440063})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31220367550849915})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.28134259581565857})
store['active_learning_steps'][74]['training']['best_epoch']=9
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9693, 'crossentropy': 0.2724166748046875}
store['active_learning_steps'][74]['eval_training']={}
store['active_learning_steps'][74]['eval_training']['epochs']=[]
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8768950700759888})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4412885904312134})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3328871428966522})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2863706350326538})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.27186131477355957})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2482537478208542})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.24239817261695862})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.22128599882125854})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2488696277141571})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.22607071697711945})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.224192276597023})
store['active_learning_steps'][74]['eval_training']['best_epoch']=8
store['active_learning_steps'][74]['acquisition']={'indices': [57922, 17503, 55054, 29501, 46491, 14540, 14679, 33090, 24061, 50960], 'labels': [8, 0, 3, -1, 6, 7, 8, 2, -1, -1], 'scores': [0.5479012131690979, 0.4589715898036957, 0.5289255380630493, 0.512100100517273, 0.4276384711265564, 0.28381645679473877, 0.4735134541988373, 0.543997198343277, 0.31666266918182373, 0.46487367153167725]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.1272954940795898})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.5199388265609741})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34519433975219727})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2804994583129883})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26968804001808167})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2776724696159363})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.23807470500469208})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.26111719012260437})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2560255825519562})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.26715728640556335})
store['active_learning_steps'][75]['training']['best_epoch']=7
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9765, 'crossentropy': 0.2195671630859375}
store['active_learning_steps'][75]['eval_training']={}
store['active_learning_steps'][75]['eval_training']['epochs']=[]
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8753869533538818})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5014001727104187})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34830641746520996})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2968922555446625})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2665131688117981})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2727818191051483})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.259755939245224})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2583257853984833})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.26573264598846436})
store['active_learning_steps'][75]['eval_training']['best_epoch']=8
store['active_learning_steps'][75]['acquisition']={'indices': [37739, 48670, 33583, 2337, 15694, 7755, 5225, 43548, 26069, 3995], 'labels': [-1, -1, -1, -1, -1, -1, -1, 8, -1, -1], 'scores': [0.489812970161438, 0.26120203733444214, 0.3709825277328491, 0.34049928188323975, 0.3544818162918091, 0.39504361152648926, 0.3433241844177246, 0.45387792587280273, 0.4916752576828003, 0.3735595941543579]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.1222875118255615})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.59175705909729})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4102036952972412})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3259297013282776})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26044362783432007})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.27341482043266296})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.276894748210907})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.261957585811615})
store['active_learning_steps'][76]['training']['best_epoch']=5
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9721, 'crossentropy': 0.253820556640625}
store['active_learning_steps'][76]['eval_training']={}
store['active_learning_steps'][76]['eval_training']['epochs']=[]
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.98257976770401})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.49806511402130127})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.40009593963623047})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.36258643865585327})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32748571038246155})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3311256170272827})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3137866258621216})
store['active_learning_steps'][76]['eval_training']['best_epoch']=7
store['active_learning_steps'][76]['acquisition']={'indices': [5812, 2764, 48494, 46255, 2475, 17263, 36197, 19895, 56108, 58972], 'labels': [-1, -1, 8, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.4141918420791626, 0.4686468839645386, 0.38279998302459717, 0.40606045722961426, 0.4380512237548828, 0.39186787605285645, 0.3941023349761963, 0.4619356393814087, 0.4119001626968384, 0.46220266819000244]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.0911767482757568})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.5023192763328552})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.39320290088653564})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3144489824771881})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27019214630126953})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2721216678619385})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.25137022137641907})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2795258164405823})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26539263129234314})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.21494725346565247})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2899892330169678})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2650349736213684})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2681119441986084})
store['active_learning_steps'][77]['training']['best_epoch']=10
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.976, 'crossentropy': 0.218123486328125}
store['active_learning_steps'][77]['eval_training']={}
store['active_learning_steps'][77]['eval_training']['epochs']=[]
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.8162788152694702})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5162656903266907})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3562632203102112})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.29648399353027344})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2526485025882721})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26788896322250366})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.24457043409347534})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2371962070465088})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2264101207256317})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.21741336584091187})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.22528675198554993})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.20738111436367035})
store['active_learning_steps'][77]['eval_training']['best_epoch']=12
store['active_learning_steps'][77]['acquisition']={'indices': [48062, 34937, 58781, 467, 3327, 30900, 41979, 1399, 37823, 2740], 'labels': [-1, -1, -1, -1, -1, 5, -1, -1, -1, -1], 'scores': [0.4954211711883545, 0.383394718170166, 0.42011165618896484, 0.559752881526947, 0.5384233593940735, 0.543998658657074, 0.604363739490509, 0.43202197551727295, 0.6590676307678223, 0.7026510834693909]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.057297945022583})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5373313426971436})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3683624267578125})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27112242579460144})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2704053819179535})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2662140429019928})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2406855821609497})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2384314239025116})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.24599286913871765})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2590782642364502})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.26716935634613037})
store['active_learning_steps'][78]['training']['best_epoch']=8
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9777, 'crossentropy': 0.2201106201171875}
store['active_learning_steps'][78]['eval_training']={}
store['active_learning_steps'][78]['eval_training']['epochs']=[]
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.9348735213279724})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5814225673675537})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3660184144973755})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.322354257106781})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2767638564109802})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27022427320480347})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.27367353439331055})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2478639781475067})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2634931206703186})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.24195142090320587})
store['active_learning_steps'][78]['eval_training']['best_epoch']=10
store['active_learning_steps'][78]['acquisition']={'indices': [32819, 58459, 43005, 50464, 15038, 29494, 19349, 1535, 39366, 16620], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.5136555433273315, 0.47162193059921265, 0.42022430896759033, 0.49898481369018555, 0.5178731083869934, 0.5135524272918701, 0.48058515787124634, 0.44676995277404785, 0.32557255029678345, 0.48454058170318604]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.049350380897522})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5670051574707031})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.34950369596481323})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3046025037765503})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2699052691459656})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24475115537643433})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.24516430497169495})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.23907431960105896})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2685781717300415})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2545946538448334})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.23722362518310547})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2772746682167053})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2570316791534424})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.27294692397117615})
store['active_learning_steps'][79]['training']['best_epoch']=11
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9776, 'crossentropy': 0.213809716796875}
store['active_learning_steps'][79]['eval_training']={}
store['active_learning_steps'][79]['eval_training']['epochs']=[]
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.9066230058670044})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4641883969306946})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3424432873725891})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.31244415044784546})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30231040716171265})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27409669756889343})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26314234733581543})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.23794883489608765})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2545168697834015})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2276812642812729})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.20918956398963928})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.18749254941940308})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.19675420224666595})
store['active_learning_steps'][79]['eval_training']['best_epoch']=12
store['active_learning_steps'][79]['acquisition']={'indices': [33176, 19503, 21062, 45368, 28692, 54991, 24325, 17640, 51417, 18403], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.4184459447860718, 0.510028600692749, 0.32236921787261963, 0.4111891984939575, 0.4867459535598755, 0.3837209939956665, 0.6065365672111511, 0.4192112684249878, 0.45927906036376953, 0.3117029666900635]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.309816837310791})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.6283568143844604})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.38335156440734863})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.28631144762039185})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.25841233134269714})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2677097022533417})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2652004063129425})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.24187111854553223})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.25512751936912537})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.22684386372566223})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9794921875, 'crossentropy': 0.23476003110408783})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2463044673204422})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.23563608527183533})
store['active_learning_steps'][80]['training']['best_epoch']=10
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9762, 'crossentropy': 0.2222882080078125}
store['active_learning_steps'][80]['eval_training']={}
store['active_learning_steps'][80]['eval_training']['epochs']=[]
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8427294492721558})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4204085171222687})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3301856517791748})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.28700006008148193})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.25947698950767517})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.24765509366989136})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2525580823421478})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2378295361995697})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.21331238746643066})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.21408650279045105})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.21938544511795044})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.1965320110321045})
store['active_learning_steps'][80]['eval_training']['best_epoch']=12
store['active_learning_steps'][80]['acquisition']={'indices': [11183, 54065, 34731, 8853, 4076, 21884, 21011, 29479, 51331, 28844], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, 2], 'scores': [0.2996009588241577, 0.385717511177063, 0.3572850227355957, 0.3000979423522949, 0.4156050682067871, 0.37886375188827515, 0.4417041540145874, 0.4186190366744995, 0.38597428798675537, 0.44581344723701477]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.168233036994934})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5832277536392212})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3819081783294678})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31866586208343506})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28311246633529663})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.25304144620895386})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.23894447088241577})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.270856112241745})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2602992057800293})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2677707374095917})
store['active_learning_steps'][81]['training']['best_epoch']=7
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9754, 'crossentropy': 0.246556298828125}
store['active_learning_steps'][81]['eval_training']={}
store['active_learning_steps'][81]['eval_training']['epochs']=[]
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9180312156677246})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5195653438568115})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3613053560256958})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3201238512992859})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2846601605415344})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2819846272468567})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2735346555709839})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2843000888824463})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.24310915172100067})
store['active_learning_steps'][81]['eval_training']['best_epoch']=9
store['active_learning_steps'][81]['acquisition']={'indices': [9, 56667, 44338, 40073, 46272, 18328, 45577, 11628, 36750, 58781], 'labels': [-1, -1, 3, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.3990144729614258, 0.4101027250289917, 0.3695688545703888, 0.40504252910614014, 0.36956608295440674, 0.4843953847885132, 0.3794078826904297, 0.455294132232666, 0.37095367908477783, 0.5803323984146118]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.2206025123596191})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.6312189102172852})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3962167799472809})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3081595301628113})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.27025383710861206})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3001726269721985})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2685176432132721})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.25970059633255005})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27820783853530884})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2801479697227478})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2530650794506073})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.27153730392456055})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.26491013169288635})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3016108274459839})
store['active_learning_steps'][82]['training']['best_epoch']=11
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.975, 'crossentropy': 0.242651220703125}
store['active_learning_steps'][82]['eval_training']={}
store['active_learning_steps'][82]['eval_training']['epochs']=[]
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8822219371795654})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4999043047428131})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35216158628463745})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3408992290496826})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28484922647476196})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.282457560300827})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2445436716079712})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.22989699244499207})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2203676700592041})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.23827975988388062})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.23973333835601807})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.21244582533836365})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.21226836740970612})
store['active_learning_steps'][82]['eval_training']['best_epoch']=13
store['active_learning_steps'][82]['acquisition']={'indices': [52922, 31526, 55788, 53102, 6416, 14634, 58568, 23890, 21290, 13376], 'labels': [-1, -1, -1, -1, 3, -1, -1, -1, -1, 3], 'scores': [0.438621461391449, 0.3242303133010864, 0.4739910364151001, 0.5057699680328369, 0.30684566497802734, 0.3265228271484375, 0.43020325899124146, 0.6365262269973755, 0.44652259349823, 0.46655726432800293]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.0998411178588867})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5893212556838989})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.34904801845550537})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2760063409805298})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2865021228790283})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.26999208331108093})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.23383468389511108})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27629539370536804})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2569805085659027})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.25721216201782227})
store['active_learning_steps'][83]['training']['best_epoch']=7
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9757, 'crossentropy': 0.2332784423828125}
store['active_learning_steps'][83]['eval_training']={}
store['active_learning_steps'][83]['eval_training']['epochs']=[]
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9557401537895203})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5425088405609131})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3855237364768982})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.350802481174469})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2778031527996063})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30183354020118713})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31170231103897095})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2503887116909027})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.22646334767341614})
store['active_learning_steps'][83]['eval_training']['best_epoch']=9
store['active_learning_steps'][83]['acquisition']={'indices': [56800, 25905, 2452, 31310, 52033, 50835, 24325, 4431, 10195, 7920], 'labels': [-1, -1, -1, 0, -1, 4, -1, -1, 0, 2], 'scores': [0.4520871639251709, 0.3421816825866699, 0.3389706611633301, 0.427146315574646, 0.6005741953849792, 0.34047210216522217, 0.4551432132720947, 0.38903582096099854, 0.46742820739746094, 0.5125918984413147]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.2216269969940186})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5573997497558594})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4296630024909973})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32084330916404724})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.307101309299469})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2848828136920929})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2885752320289612})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2750357687473297})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.25030243396759033})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2596917152404785})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27797138690948486})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2689847946166992})
store['active_learning_steps'][84]['training']['best_epoch']=9
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9732, 'crossentropy': 0.249730908203125}
store['active_learning_steps'][84]['eval_training']={}
store['active_learning_steps'][84]['eval_training']['epochs']=[]
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.9515554904937744})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5736720561981201})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3885048031806946})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32782405614852905})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29604199528694153})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30286431312561035})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.28660452365875244})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.22216813266277313})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.23910795152187347})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2339092493057251})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2532428801059723})
store['active_learning_steps'][84]['eval_training']['best_epoch']=8
