store = {}
store['timestamp']=1621471718
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=24']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=24
store['worker_id']=24
store['num_workers']=80
store['config']={'seed': 1259, 'uniform_ood': True, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('FastFashionMNIST Train (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 3792, 5573, 45567, 10508, 2728, 21423, 396, 49512, 31444]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.1025757789611816})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.4431161880493164})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.5705442428588867})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.9611449241638184})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.8881964683532715})
store['active_learning_steps'][0]['training']['best_epoch']=2
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.7001, 'crossentropy': 2.0806759765625}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 26073], ['id', 25309], ['id', 5618], ['id', 22675], ['id', 22845]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.284948465441916, 2.329929842851044, 3.147073361658668, 3.728489351725373, 4.093937611116963]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.0622339248657227})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.2954320907592773})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.567168712615967})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.4871251583099365})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.9337635040283203})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.898562431335449})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.8832168579101562})
store['active_learning_steps'][1]['training']['best_epoch']=4
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6979, 'crossentropy': 2.24119453125}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 4745], ['id', 26496], ['id', 26333], ['id', 27130], ['id', 53574]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.2005650969735429, 2.217169670083282, 3.0283494463954677, 3.6370879580751634, 4.032289374219197]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.9911329746246338})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.229194402694702})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.540250062942505})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.6183745861053467})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.470987319946289})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.6330628395080566})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.7835874557495117})
store['active_learning_steps'][2]['training']['best_epoch']=4
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7082, 'crossentropy': 2.23629609375}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 42749], ['id', 38352], ['id', 7967], ['id', 19942], ['id', 30646]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [1.238842695050152, 2.3251584400374448, 3.203698348176827, 3.795776500865138, 4.150682391255067]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.6027958393096924})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.075608491897583})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.4731674194335938})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.157163619995117})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.4920382499694824})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.499391555786133})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.6025123596191406})
store['active_learning_steps'][3]['training']['best_epoch']=4
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7302, 'crossentropy': 1.9440486328125}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 46890], ['id', 1812], ['id', 3370], ['id', 36427], ['id', 52138]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [1.260141087452927, 2.370699881443035, 3.1949690379375877, 3.782590209385482, 4.1399256020591455]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.5866799354553223})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 2.1176376342773438})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.2619361877441406})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.131391763687134})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 2.4923136234283447})
store['active_learning_steps'][4]['training']['best_epoch']=2
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7444, 'crossentropy': 1.72105859375}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 46144], ['id', 25538], ['id', 29869], ['id', 34631], ['id', 26563]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [1.1194763755200823, 2.130324991793587, 2.93662276912327, 3.5312052368628786, 3.9212997178347093]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.623103141784668})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.7610557079315186})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.8312020301818848})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.7551188468933105})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.911996841430664})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 2.0860915184020996})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 2.051121473312378})
store['active_learning_steps'][5]['training']['best_epoch']=4
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8014, 'crossentropy': 1.46199931640625}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 17055], ['id', 58519], ['id', 20035], ['id', 15005], ['id', 22911]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [1.1943585042382008, 2.218528162256159, 3.0607530849796873, 3.6721535417375986, 4.059868778904529]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.2705954313278198})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.4793142080307007})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.6362788677215576})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.7434755563735962})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.9247552156448364})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.7748315334320068})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.7589032649993896})
store['active_learning_steps'][6]['training']['best_epoch']=4
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7895, 'crossentropy': 1.4500076171875}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 37383], ['id', 7924], ['id', 31883], ['id', 24995], ['id', 30451]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.1101266843239217, 2.149273890022516, 2.961953573496718, 3.567331856857513, 3.980452800544141]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.3404591083526611})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.3149476051330566})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.6445657014846802})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.8705546855926514})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.6755650043487549})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.812, 'crossentropy': 1.1422140625}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 23104], ['id', 37843], ['id', 49992], ['id', 27247], ['id', 23982]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1200692667761531, 2.0519204789133845, 2.8637100744737545, 3.4731955887428425, 3.884521944572434]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.1186788082122803})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.3337159156799316})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.3835046291351318})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.5648137331008911})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.5635862350463867})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.573103427886963})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.8592042922973633})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.7663681507110596})
store['active_learning_steps'][8]['training']['best_epoch']=5
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8303, 'crossentropy': 1.2539619140625}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 36686], ['id', 24347], ['id', 19869], ['id', 8958], ['id', 43575]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.2235683918841849, 2.304651938051667, 3.1775211222611137, 3.7989804306298094, 4.170675582809356]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.012506365776062})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.1647212505340576})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.3856077194213867})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.4918169975280762})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.4011993408203125})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.4081299304962158})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.5259678363800049})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.6636686325073242})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.6615004539489746})
store['active_learning_steps'][9]['training']['best_epoch']=6
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8437, 'crossentropy': 1.2268865234375}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 46580], ['id', 16951], ['id', 50403], ['id', 1652], ['id', 40208]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.2330128873730646, 2.353424233539221, 3.2425277490061672, 3.8652372234276786, 4.219801338509869]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9816714525222778})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.1595652103424072})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.2237783670425415})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.4094433784484863})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.448686122894287})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.503278374671936})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.5250921249389648})
store['active_learning_steps'][10]['training']['best_epoch']=4
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8438, 'crossentropy': 1.1035310546875}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 49893], ['id', 40549], ['id', 31090], ['id', 32323], ['id', 37339]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1161736690642576, 2.1397867485629365, 2.990704544336033, 3.5949463128451544, 3.996334022228134]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9296550750732422})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.9747559428215027})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.2212388515472412})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.085208773612976})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.1569292545318604})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.0773885250091553})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.1634762287139893})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.3078711032867432})
store['active_learning_steps'][11]['training']['best_epoch']=5
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8821, 'crossentropy': 0.9206234375}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 10153], ['id', 16989], ['id', 52959], ['id', 46126], ['id', 57191]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1412567328254846, 2.227636309977801, 3.070176002740319, 3.6721852094888963, 4.071750751000078]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9415372014045715})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.9271541833877563})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9284849166870117})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.9014034271240234})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.0975875854492188})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.1657286882400513})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8707, 'crossentropy': 0.86313837890625}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 37048], ['id', 24426], ['id', 13045], ['id', 46132], ['id', 5630]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0467843956999716, 1.9777616539029212, 2.7802780479837477, 3.4118635789156633, 3.8401848610882325]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9509481191635132})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.9670649766921997})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.9100307822227478})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9173961281776428})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.009469747543335})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.0643203258514404})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.1743777990341187})
store['active_learning_steps'][13]['training']['best_epoch']=4
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8772, 'crossentropy': 0.8537673828125}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 11708], ['id', 57221], ['id', 19111], ['id', 52582], ['id', 4909]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.0771762006294774, 2.0620650738239616, 2.8746282975528814, 3.5027400315461517, 3.9214996800498394]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 0.9983612895011902})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8825374841690063})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.9037847518920898})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.9173102378845215})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.1156322956085205})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.1324739456176758})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.006779432296753})
store['active_learning_steps'][14]['training']['best_epoch']=4
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8738, 'crossentropy': 0.83039716796875}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 13074], ['id', 50912], ['id', 16102], ['id', 49537], ['id', 45602]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0149123328704799, 1.9405383104213811, 2.7884880038231525, 3.4310827869189886, 3.8784480876006207]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.0558271408081055})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.944280207157135})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.0184880495071411})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.039379358291626})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.1087360382080078})
store['active_learning_steps'][15]['training']['best_epoch']=2
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8691, 'crossentropy': 0.788054345703125}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 57334], ['id', 14896], ['id', 58560], ['id', 58470], ['id', 12757]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.9364573649366923, 1.7610318349899803, 2.5026989376923066, 3.099338515116747, 3.54944068388145]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9344666600227356})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8083540201187134})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7667126655578613})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.764248251914978})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8839428424835205})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8774, 'crossentropy': 0.74286494140625}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 34800], ['id', 19099], ['id', 28783], ['id', 10038], ['id', 10244]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9251011101915871, 1.798976963482211, 2.4820697891407377, 3.043558614128316, 3.487555402132778]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8812530636787415})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6819841861724854})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6511535048484802})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6663063764572144})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7562659978866577})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7071057558059692})
store['active_learning_steps'][17]['training']['best_epoch']=3
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9059, 'crossentropy': 0.62568876953125}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 45026], ['id', 27458], ['id', 37574], ['id', 49448], ['id', 12181]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.964663091127125, 1.854890214964028, 2.613596690906835, 3.239251747938793, 3.7044725433835506]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.9227879047393799})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6454097032546997})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6136161088943481})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6209109425544739})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6509547233581543})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6564831733703613})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6801237463951111})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7940119504928589})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6824856996536255})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6799331307411194})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7407411336898804})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7423281669616699})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.9377331137657166})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.797887921333313})
store['active_learning_steps'][18]['training']['best_epoch']=11
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9087, 'crossentropy': 0.725790234375}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 49890], ['id', 57608], ['id', 18680], ['id', 52140], ['id', 41434]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [1.2180325658781859, 2.3667793076047543, 3.23468278901323, 3.830379044219585, 4.189767835804373]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8370642066001892})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.717555046081543})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6311454176902771})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6567596793174744})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6162631511688232})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7447868585586548})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7797514200210571})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7576160430908203})
store['active_learning_steps'][19]['training']['best_epoch']=5
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9132, 'crossentropy': 0.606984619140625}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 13942], ['id', 50562], ['id', 7434], ['id', 36417], ['id', 26850]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0595391723437229, 1.9723710455830292, 2.757690452199503, 3.375127166397073, 3.823600765106523]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9614521265029907})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5599197745323181})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5967553853988647})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5721721649169922})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5625022649765015})
store['active_learning_steps'][20]['training']['best_epoch']=2
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9045, 'crossentropy': 0.560079052734375}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 51869], ['id', 36783], ['id', 2078], ['id', 35864], ['id', 3972]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8407466932760863, 1.5968420332114732, 2.2709173567527774, 2.8461415848517193, 3.3104698993764394]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.13649320602417})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.637325644493103})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5330668687820435})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5886073112487793})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6342848539352417})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5972917079925537})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6720604300498962})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6611009836196899})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6828646659851074})
store['active_learning_steps'][21]['training']['best_epoch']=6
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9231, 'crossentropy': 0.582659423828125}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 35401], ['id', 14825], ['id', 45446], ['id', 54885], ['id', 43126]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0873175415040572, 2.0985913811196717, 2.962417838021997, 3.5844058485542467, 3.9932358268936596]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9627095460891724})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6939257383346558})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5662764310836792})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6179556846618652})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6095879077911377})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.712028980255127})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6565080881118774})
store['active_learning_steps'][22]['training']['best_epoch']=4
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9159, 'crossentropy': 0.589605517578125}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 2184], ['id', 41933], ['id', 23086], ['id', 10256], ['id', 36818]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [1.0478484124564877, 1.9806347292511681, 2.8163209446724817, 3.4386758266384083, 3.8530849002652685]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9010967016220093})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6050156354904175})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6042376756668091})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5985450148582458})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6772099733352661})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6511386632919312})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6526448726654053})
store['active_learning_steps'][23]['training']['best_epoch']=4
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9093, 'crossentropy': 0.591096484375}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 8714], ['id', 52801], ['id', 46941], ['id', 32471], ['id', 11304]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.018559692107426, 1.9803774880190654, 2.7808411532940784, 3.403349527868908, 3.8521995404330944]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.0628340244293213})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.576359212398529})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6209343671798706})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6004481315612793})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5764791965484619})
store['active_learning_steps'][24]['training']['best_epoch']=2
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9169, 'crossentropy': 0.575234765625}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 55128], ['id', 19298], ['id', 19590], ['id', 17849], ['id', 22200]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.820020713326006, 1.5923864335639601, 2.2691945555072017, 2.851885499589409, 3.317536693998134]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.0046874284744263})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5926348567008972})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5811021327972412})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5400069952011108})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5624561309814453})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5354318618774414})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5951256155967712})
store['active_learning_steps'][25]['training']['best_epoch']=4
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9244, 'crossentropy': 0.51853095703125}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 46832], ['id', 47473], ['id', 14100], ['id', 7406], ['id', 1674]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [1.0517766406665727, 1.9796087700249463, 2.7885765235474924, 3.409340110991339, 3.853430239248323]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.0640439987182617})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6507378816604614})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6014338731765747})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5931810140609741})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5730621814727783})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6254091262817383})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6192584037780762})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6125471591949463})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6734040975570679})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.635303258895874})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6303625106811523})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6357806324958801})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6547237634658813})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6851759552955627})
store['active_learning_steps'][26]['training']['best_epoch']=11
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9194, 'crossentropy': 0.637364111328125}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 109], ['id', 4822], ['id', 43636], ['id', 18150], ['id', 52169]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.2028507347594797, 2.2853107162088784, 3.1552125703997786, 3.7829946279480025, 4.151591415764566]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.0039710998535156})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5738346576690674})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5267924666404724})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4843728542327881})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5432986617088318})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5323835611343384})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5895006656646729})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9257, 'crossentropy': 0.493411328125}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 47365], ['id', 55042], ['id', 53872], ['id', 2292], ['id', 17415]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9134970231009139, 1.7845124717591974, 2.566334091707297, 3.1726470684770476, 3.642272194463561]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9859583377838135})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5922268629074097})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5528157949447632})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.49791961908340454})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5516892671585083})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5138194561004639})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5597786903381348})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5563806295394897})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5212357044219971})
store['active_learning_steps'][28]['training']['best_epoch']=6
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9295, 'crossentropy': 0.502942431640625}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 56528], ['id', 34328], ['id', 43745], ['id', 1239], ['id', 52771]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0722045936828213, 2.0260432753760034, 2.8482751359287803, 3.487413185865589, 3.9375455090151803]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.0741400718688965})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5733311772346497})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5558130741119385})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.48515158891677856})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.47319459915161133})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5506576299667358})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5541751980781555})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9317, 'crossentropy': 0.4656103515625}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 39818], ['id', 42415], ['id', 33812], ['id', 50403], ['id', 24479]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.012583772122538, 1.9192395846200876, 2.7103376085483397, 3.3247882424927173, 3.7700639038264088]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.0244483947753906})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6779005527496338})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.49233055114746094})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5182998180389404})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5669306516647339})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5824914574623108})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5170358419418335})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5774908065795898})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5625631809234619})
store['active_learning_steps'][30]['training']['best_epoch']=6
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.935, 'crossentropy': 0.53279853515625}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 32880], ['id', 15450], ['id', 1634], ['id', 59747], ['id', 20820]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [1.1170836674488118, 2.114602673707209, 2.950461379397865, 3.568049784704951, 3.9822286248081555]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.1306369304656982})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7180742025375366})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.528161883354187})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5058073401451111})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.493728905916214})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5498571395874023})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5375538468360901})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6471380591392517})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6426776647567749})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.6316623687744141})
store['active_learning_steps'][31]['training']['best_epoch']=7
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9277, 'crossentropy': 0.5240697265625}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 57714], ['id', 13998], ['id', 36408], ['id', 43702], ['id', 1075]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [1.0564178380095903, 2.048235816991569, 2.878445059480545, 3.515194358553938, 3.944374532554648]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.0275702476501465})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6189239621162415})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5607777833938599})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.540263831615448})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5267850756645203})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5478689670562744})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5596630573272705})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6640529036521912})
store['active_learning_steps'][32]['training']['best_epoch']=5
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9298, 'crossentropy': 0.48913818359375}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 4153], ['id', 48006], ['id', 1573], ['id', 34199], ['id', 49364]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.959268554775631, 1.8334733303089767, 2.612417737718567, 3.2385111021319197, 3.6888199145048697]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.0044125318527222})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5753644704818726})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.48082810640335083})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5253101587295532})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4374854564666748})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4806499481201172})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.45895853638648987})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5090383291244507})
store['active_learning_steps'][33]['training']['best_epoch']=5
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9413, 'crossentropy': 0.411522802734375}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 30418], ['id', 28199], ['id', 13247], ['id', 22139], ['id', 41540]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9102118929698007, 1.7461056438752696, 2.4953792202803182, 3.1148240959392783, 3.607508172944721]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.0444542169570923})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.605162501335144})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4844839572906494})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.45689576864242554})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.49108392000198364})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.45065373182296753})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.520795464515686})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5256890058517456})
store['active_learning_steps'][34]['training']['best_epoch']=5
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9323, 'crossentropy': 0.479910546875}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 34847], ['id', 13149], ['id', 15723], ['id', 55774], ['id', 15276]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.9056599223369943, 1.7455685235236698, 2.4982570000756805, 3.115830414057613, 3.587658899304519]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.9691128730773926})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5792218446731567})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.46491116285324097})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.39734670519828796})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4303366541862488})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.41717463731765747})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4230572581291199})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4074670374393463})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.45874637365341187})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.46157270669937134})
store['active_learning_steps'][35]['training']['best_epoch']=7
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9432, 'crossentropy': 0.432301953125}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 15948], ['id', 34743], ['id', 22286], ['id', 49354], ['id', 12650]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.048153828735997, 2.0005682298176146, 2.78500439473917, 3.41140333924948, 3.854748699512089]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.9777575731277466})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.6033071279525757})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4560191035270691})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.44286036491394043})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4385583996772766})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.41553372144699097})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4290087819099426})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.483865350484848})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.44030725955963135})
store['active_learning_steps'][36]['training']['best_epoch']=6
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9481, 'crossentropy': 0.400738671875}
