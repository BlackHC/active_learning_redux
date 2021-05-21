store = {}
store['timestamp']=1621471693
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=16']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=16
store['worker_id']=16
store['num_workers']=80
store['config']={'seed': 1251, 'uniform_ood': True, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('FastFashionMNIST Train (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 3792, 5573, 45567, 10508, 2728, 21423, 396, 49512, 31444]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.2178070545196533})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.3111119270324707})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.5687506198883057})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.662446975708008})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.6394803524017334})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.580888271331787})
store['active_learning_steps'][0]['training']['best_epoch']=3
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.7173, 'crossentropy': 2.31158984375}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.3455103635787964})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.4071121215820312})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.4229081869125366})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.3989324569702148})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.422612190246582})
store['active_learning_steps'][0]['eval_training']['best_epoch']=4
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 47889], ['id', 23919], ['id', 17080], ['id', 8680], ['id', 5413]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.033178105171566, 1.8325661185795195, 2.373435462175154, 2.7582169573157325, 2.9786643008917464]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.4937806129455566})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.6859087944030762})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.0135397911071777})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.0629494190216064})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.3204708099365234})
store['active_learning_steps'][1]['training']['best_epoch']=2
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7263, 'crossentropy': 1.51893994140625}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.3219940662384033})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.272615909576416})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.379015326499939})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.3795981407165527})
store['active_learning_steps'][1]['eval_training']['best_epoch']=1
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 50403], ['id', 30740], ['id', 36432], ['id', 16866], ['id', 14383]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6236962490694833, 1.1731322067148167, 1.5921351385132096, 1.8892511409761, 2.043869960419679]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.6160469055175781})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.044581651687622})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.9117472171783447})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.225978374481201})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.3603317737579346})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.1492300033569336})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.207866668701172})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.478250026702881})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.3177266120910645})
store['active_learning_steps'][2]['training']['best_epoch']=6
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7143, 'crossentropy': 1.8846328125}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.6169267892837524})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.7795021533966064})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.7430596351623535})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.7845224142074585})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.916365146636963})
store['active_learning_steps'][2]['eval_training']['best_epoch']=2
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 28452], ['id', 635], ['id', 4611], ['id', 4743], ['id', 13371]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7898885583752735, 1.4188849825594532, 1.9440934525311553, 2.3457117107086285, 2.6105116944860596]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.7984000444412231})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.9122345447540283})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.2948012351989746})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.4414515495300293})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.433873414993286})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.6004185676574707})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.2002463340759277})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.686917781829834})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.588670253753662})
store['active_learning_steps'][3]['training']['best_epoch']=6
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6853, 'crossentropy': 2.334684375}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.4972681999206543})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.6834547519683838})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.6806640625})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.6958016157150269})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.7201534509658813})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.7051441669464111})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.7106969356536865})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.686769962310791})
store['active_learning_steps'][3]['eval_training']['best_epoch']=5
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 57523], ['id', 9874], ['id', 12655], ['id', 20518], ['id', 56673]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.7289646313992801, 1.3752045793902519, 1.8759235420568974, 2.2649879175654046, 2.5197647499943003]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.672850251197815})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.9589383602142334})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.223379373550415})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.2951812744140625})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.4316213130950928})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.5518300533294678})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.563473701477051})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.5627660751342773})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.3352723121643066})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.5070090293884277})
store['active_learning_steps'][4]['training']['best_epoch']=7
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6994, 'crossentropy': 2.353542578125}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.612781286239624})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.7144721746444702})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.5742802619934082})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.6739513874053955})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.8431198596954346})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.691171646118164})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 65], ['id', 27930], ['id', 7726], ['id', 23877], ['id', 29002]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.6788053557543461, 1.2379956884882088, 1.7223214501341992, 2.0512042631188625, 2.2717343256381817]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.5097975730895996})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.7010307312011719})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.9842694997787476})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.3157572746276855})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.022955894470215})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.4232773780822754})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.2939631938934326})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.379322052001953})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.7612967491149902})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.3948593139648438})
store['active_learning_steps'][5]['training']['best_epoch']=7
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7268, 'crossentropy': 2.04900078125}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.5853607654571533})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.696559190750122})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.6989314556121826})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.6809802055358887})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.6208019256591797})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.674261212348938})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.7720978260040283})
store['active_learning_steps'][5]['eval_training']['best_epoch']=4
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 10669], ['id', 52975], ['id', 59726], ['id', 32301], ['id', 11705]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7156028723922572, 1.323926811299768, 1.7986547159138202, 2.140901178695098, 2.364552256214804]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.6022539138793945})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.7585783004760742})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.8583579063415527})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.2033498287200928})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.1770870685577393})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.124302864074707})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.1882271766662598})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 2.2610435485839844})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 2.0949819087982178})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.2328004837036133})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.7821764945983887})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.2410225868225098})
store['active_learning_steps'][6]['training']['best_epoch']=9
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7466, 'crossentropy': 1.9771689453125}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.4486933946609497})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.5958755016326904})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.576399803161621})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.497119665145874})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.3853187561035156})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.4758176803588867})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.5403834581375122})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.5465596914291382})
store['active_learning_steps'][6]['eval_training']['best_epoch']=5
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 11193], ['id', 8339], ['id', 41459], ['id', 25577], ['id', 7772]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8088480153053408, 1.4825248889607354, 2.021190485342929, 2.395319700972448, 2.6260762611148745]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.4476910829544067})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.3768131732940674})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.5197139978408813})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.62751042842865})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.793570876121521})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.878061294555664})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 2.1124391555786133})
store['active_learning_steps'][7]['training']['best_epoch']=4
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7711, 'crossentropy': 1.40075087890625}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.215741515159607})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.1755670309066772})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.1648790836334229})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.0871797800064087})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.126387357711792})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.103988766670227})
store['active_learning_steps'][7]['eval_training']['best_epoch']=4
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 20157], ['id', 48248], ['id', 49773], ['id', 15134], ['id', 4502]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6361435882155155, 1.2254126373375294, 1.7430410673219843, 2.0943739528969054, 2.3777924877790877]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.2865211963653564})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.4390382766723633})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.5326550006866455})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.7797281742095947})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.8070614337921143})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.8115332126617432})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.6972171068191528})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.7163043022155762})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.8811514377593994})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.8240275382995605})
store['active_learning_steps'][8]['training']['best_epoch']=7
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7749, 'crossentropy': 1.6944767578125}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.1983699798583984})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.296144962310791})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.250518560409546})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.2349638938903809})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.1472846269607544})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.265744686126709})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.2001562118530273})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.2053216695785522})
store['active_learning_steps'][8]['eval_training']['best_epoch']=5
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 22493], ['id', 50698], ['id', 22281], ['id', 34306], ['id', 15461]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5742362154800481, 1.1015085825047426, 1.5097016373928174, 1.8101349494366268, 2.0163342644341746]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.3743577003479004})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.27901291847229})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.5588127374649048})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.6992614269256592})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.7804067134857178})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 2.0078229904174805})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.9655861854553223})
store['active_learning_steps'][9]['training']['best_epoch']=4
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.7874, 'crossentropy': 1.51881025390625}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.2058665752410889})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.1136085987091064})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.1089529991149902})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.094621181488037})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.0167920589447021})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 0.9870414733886719})
store['active_learning_steps'][9]['eval_training']['best_epoch']=6
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 8744], ['id', 6284], ['id', 43656], ['id', 17046], ['id', 22163]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.6980766210612308, 1.3101717632444347, 1.7715505702312768, 2.0681193772409605, 2.252833041103333]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.2404191493988037})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.497176170349121})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.5042932033538818})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.6732850074768066})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.8654807806015015})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.8856861591339111})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 2.108745813369751})
store['active_learning_steps'][10]['training']['best_epoch']=4
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.7949, 'crossentropy': 1.4698857421875}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.1536256074905396})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.0874907970428467})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.1089990139007568})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.1321983337402344})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.1371867656707764})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.1198582649230957})
store['active_learning_steps'][10]['eval_training']['best_epoch']=3
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 58967], ['id', 23441], ['id', 13516], ['id', 52057], ['id', 28102]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5526485894828889, 1.0890434416302777, 1.5500431752593107, 1.9231205134639433, 2.1879598193990266]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.2314870357513428})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.3633095026016235})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.4995068311691284})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.6462687253952026})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.7974364757537842})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.6977413892745972})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.8975704908370972})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.966246485710144})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.988468050956726})
store['active_learning_steps'][11]['training']['best_epoch']=6
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8081, 'crossentropy': 1.5156671875}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.1367807388305664})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.1376168727874756})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.1147637367248535})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.18558931350708})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.0975422859191895})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.1691632270812988})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.1984648704528809})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.1221308708190918})
store['active_learning_steps'][11]['eval_training']['best_epoch']=8
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 31009], ['id', 36686], ['id', 512], ['id', 39627], ['id', 25442]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8300344952330987, 1.499212380925092, 2.0557902623691326, 2.437769617776694, 2.713430703936748]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.1360012292861938})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.3318730592727661})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.398998498916626})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.2875840663909912})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.6325795650482178})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.6134072542190552})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.6659955978393555})
store['active_learning_steps'][12]['training']['best_epoch']=4
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8298, 'crossentropy': 1.16995009765625}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.110198974609375})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.062922716140747})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.0157641172409058})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.9416052103042603})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.8918222188949585})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.9489508867263794})
store['active_learning_steps'][12]['eval_training']['best_epoch']=4
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 17761], ['id', 23021], ['id', 12965], ['id', 42246], ['id', 57484]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6594117293640862, 1.1613133054163196, 1.5752605081346007, 1.881800039504376, 2.1012142735116104]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.1372811794281006})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.2434828281402588})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.2663429975509644})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.4600751399993896})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.5027034282684326})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8161, 'crossentropy': 1.02482763671875}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.202107310295105})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 0.9363250732421875})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.8692889213562012})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 0.8890624046325684})
store['active_learning_steps'][13]['eval_training']['best_epoch']=3
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 9158], ['id', 5259], ['id', 37735], ['id', 45332], ['id', 48925]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5945016691180811, 1.1059193573870578, 1.4900402130421142, 1.7826436775190198, 1.9776921085001824]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.1488842964172363})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.0616919994354248})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.1182318925857544})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.2689323425292969})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.344186782836914})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.4031658172607422})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.433298110961914})
store['active_learning_steps'][14]['training']['best_epoch']=4
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8393, 'crossentropy': 1.0682728515625}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.1145124435424805})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.0379910469055176})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 0.9050917625427246})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.9230877161026001})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.895186185836792})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.9313378930091858})
store['active_learning_steps'][14]['eval_training']['best_epoch']=5
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 48102], ['id', 22591], ['id', 134], ['id', 27473], ['id', 17710]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6089502749910524, 1.1814559089971741, 1.6440392416472704, 1.9921446360730277, 2.2425868388440353]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.9825834035873413})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.9965038299560547})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.0169483423233032})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.0136613845825195})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.108298420906067})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.2027435302734375})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.3393826484680176})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.3204739093780518})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.4062732458114624})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.3627848625183105})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.475074291229248})
store['active_learning_steps'][15]['training']['best_epoch']=8
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8439, 'crossentropy': 1.25871259765625}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.002021074295044})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 0.9338510632514954})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.9458933472633362})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8590757846832275})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.8652973175048828})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9279118776321411})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.8221051692962646})
store['active_learning_steps'][15]['eval_training']['best_epoch']=4
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 16188], ['id', 50711], ['id', 1129], ['id', 4451], ['id', 16836]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.6445417922212007, 1.2549041079238696, 1.7628119028646427, 2.1377514395468395, 2.41410603266993]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.15641188621521})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.0552740097045898})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.019197702407837})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.1979730129241943})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.1821446418762207})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.4159765243530273})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.2781931161880493})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.1951735019683838})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.3616487979888916})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.2857569456100464})
store['active_learning_steps'][16]['training']['best_epoch']=7
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8485, 'crossentropy': 1.08850771484375}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.137474775314331})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9756598472595215})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.8582056760787964})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.8642556071281433})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8681703209877014})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.7681993246078491})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.7759212851524353})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.7852778434753418})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.7295662760734558})
store['active_learning_steps'][16]['eval_training']['best_epoch']=6
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 45005], ['id', 54520], ['id', 10992], ['id', 5956], ['id', 35557]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8065165028079778, 1.5120928921932653, 2.084343447721173, 2.4570386050690507, 2.7148129085073345]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.0692933797836304})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.8552988767623901})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9002271890640259})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9406962394714355})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.0922825336456299})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.2179055213928223})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.134223461151123})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.0812790393829346})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.2770884037017822})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.3950073719024658})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.2982126474380493})
store['active_learning_steps'][17]['training']['best_epoch']=8
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8598, 'crossentropy': 1.0339908203125}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.1520284414291382})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.9117154479026794})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.9051145315170288})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.8931542634963989})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8559110164642334})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.8928143978118896})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8232817649841309})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.8495892286300659})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.7665335536003113})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.7787868976593018})
store['active_learning_steps'][17]['eval_training']['best_epoch']=9
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 14121], ['id', 19702], ['id', 38403], ['id', 51436], ['id', 41984]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6765536180317357, 1.2925296407635596, 1.8149038740389818, 2.202021745693947, 2.4654179751335716]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.0025438070297241})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.9863206148147583})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.081310510635376})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.0291452407836914})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.0778422355651855})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.1910512447357178})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.1255464553833008})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.1159042119979858})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.395146131515503})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.5006380081176758})
store['active_learning_steps'][18]['training']['best_epoch']=7
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8601, 'crossentropy': 1.039628125}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.1891273260116577})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.0594537258148193})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.7753102779388428})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.8587923049926758})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.8238892555236816})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8045102953910828})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.7987346649169922})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.778962254524231})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.7857703566551208})
store['active_learning_steps'][18]['eval_training']['best_epoch']=6
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 31090], ['id', 42140], ['id', 10073], ['id', 50417], ['id', 29839]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6773214372667351, 1.2900641652399818, 1.7699064098898623, 2.104670984732154, 2.3187519840354742]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.1960082054138184})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.2639176845550537})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.3366904258728027})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.4393616914749146})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.39178466796875})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.2689104080200195})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.306999921798706})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.6386277675628662})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.5910604000091553})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.508322834968567})
store['active_learning_steps'][19]['training']['best_epoch']=7
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8417, 'crossentropy': 1.37166328125}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.2435376644134521})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.0194306373596191})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9486512541770935})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.9903260469436646})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.0537021160125732})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9605366587638855})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9405038952827454})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.922130823135376})
store['active_learning_steps'][19]['eval_training']['best_epoch']=5
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 52937], ['id', 24998], ['id', 40571], ['id', 224], ['id', 5248]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6503721708834678, 1.2409014466896315, 1.70180168295794, 2.078803719002091, 2.356038089647529]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.0876197814941406})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.9059038758277893})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.0348957777023315})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.180382251739502})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.303575038909912})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.1526849269866943})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.1828235387802124})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.1576814651489258})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.210270643234253})
store['active_learning_steps'][20]['training']['best_epoch']=6
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8572, 'crossentropy': 1.07277783203125}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.1198766231536865})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.0444364547729492})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.9683655500411987})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.9741413593292236})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.917401134967804})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.924369215965271})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.9047294855117798})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8481509685516357})
store['active_learning_steps'][20]['eval_training']['best_epoch']=8
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 39424], ['id', 33659], ['id', 31124], ['id', 15167], ['id', 17044]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.6452621344952052, 1.185826405214049, 1.611365907328206, 1.9310316772178258, 2.140919746286853]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.0283194780349731})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9833667874336243})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.0906486511230469})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.0505092144012451})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.1207218170166016})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.159637689590454})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.179616093635559})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.3098241090774536})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.2715789079666138})
store['active_learning_steps'][21]['training']['best_epoch']=6
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.8583, 'crossentropy': 1.03419111328125}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.0607776641845703})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9309216737747192})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9498840570449829})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8430211544036865})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7622538208961487})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7279934883117676})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7727200984954834})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8125796318054199})
store['active_learning_steps'][21]['eval_training']['best_epoch']=5
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 40866], ['id', 25479], ['id', 54056], ['id', 8568], ['id', 57573]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6260202569488758, 1.197236877724678, 1.625224083971467, 1.9516332100577802, 2.190673305711031]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 0.9764676094055176})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.714379072189331})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8131870031356812})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6843063831329346})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8206797242164612})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7993195056915283})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9723824262619019})
store['active_learning_steps'][22]['training']['best_epoch']=4
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8821, 'crossentropy': 0.68360029296875}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.0205698013305664})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7050361633300781})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.6584345698356628})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.5835111737251282})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.5761076211929321})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.5740066766738892})
store['active_learning_steps'][22]['eval_training']['best_epoch']=4
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 24097], ['id', 32206], ['id', 15500], ['id', 42254], ['id', 48888]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.6088044829535066, 1.1307010015727483, 1.5274949372786475, 1.8122263381571573, 1.9944690167232073]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.0859014987945557})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6922742128372192})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7853876948356628})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7651373744010925})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8638015985488892})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8783347010612488})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8137362003326416})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8669946789741516})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8460426330566406})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8683907985687256})
store['active_learning_steps'][23]['training']['best_epoch']=7
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.8836, 'crossentropy': 0.799419873046875}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.0504132509231567})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.7663167715072632})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6993582844734192})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6361852884292603})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6357582807540894})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6263874173164368})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.5781913995742798})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5708747506141663})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6008611917495728})
store['active_learning_steps'][23]['eval_training']['best_epoch']=8
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 18408], ['id', 50317], ['id', 36985], ['id', 29335], ['id', 40208]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7010975941873123, 1.3071977154281686, 1.788056350572984, 2.1062712162550774, 2.298066842326203]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.948912501335144})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7183804512023926})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7092985510826111})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7569316625595093})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8093851804733276})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7740426063537598})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8780770301818848})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8333063125610352})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.779975175857544})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8220387697219849})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8202605843544006})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.821103572845459})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7635905742645264})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8494082689285278})
store['active_learning_steps'][24]['training']['best_epoch']=11
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.8924, 'crossentropy': 0.78823720703125}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 0.9559799432754517})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6796268224716187})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.714583158493042})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5834357738494873})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.5945799350738525})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.5853267908096313})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.5369739532470703})
store['active_learning_steps'][24]['eval_training']['best_epoch']=4
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 59361], ['id', 48933], ['id', 57139], ['id', 58812], ['id', 12688]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7421577211746677, 1.3732283684918798, 1.8735765799027728, 2.219796382708849, 2.430382943654595]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.9734780192375183})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6617895364761353})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6661519408226013})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7115939855575562})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6476307511329651})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6732949018478394})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7379351258277893})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7299450635910034})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.821334719657898})
store['active_learning_steps'][25]['training']['best_epoch']=6
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9128, 'crossentropy': 0.606543798828125}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9111966490745544})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6647049188613892})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.5696688294410706})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5035258531570435})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5385624170303345})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.47356924414634705})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.4825482964515686})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.49897921085357666})
store['active_learning_steps'][25]['eval_training']['best_epoch']=7
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 54598], ['id', 35606], ['id', 38842], ['id', 19844], ['id', 27972]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6230866319205031, 1.19065412786576, 1.6631588617571582, 2.0083024595184735, 2.250400904518255]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9494962096214294})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6740111708641052})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7126900553703308})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6927889585494995})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.650527834892273})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6510252952575684})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6598001718521118})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7334363460540771})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7903950214385986})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7877885103225708})
store['active_learning_steps'][26]['training']['best_epoch']=7
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9022, 'crossentropy': 0.647132421875}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.9226895570755005})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6413691639900208})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5272827744483948})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5534825325012207})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5025431513786316})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5236760377883911})
store['active_learning_steps'][26]['eval_training']['best_epoch']=3
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 19138], ['id', 19190], ['id', 58000], ['id', 46524], ['id', 25998]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.5652920759271431, 1.0777114149654725, 1.4760247328327374, 1.7972412765929695, 2.0418328247398723]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.0323677062988281})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.636493444442749})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5825361013412476})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5787985324859619})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6076928377151489})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5515705347061157})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5764646530151367})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5925284624099731})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6430982351303101})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6592150330543518})
store['active_learning_steps'][27]['training']['best_epoch']=7
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9224, 'crossentropy': 0.5513861328125}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.8865250945091248})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6167001724243164})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5372985601425171})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5445429682731628})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5112277269363403})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5162877440452576})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.4885849952697754})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5140891075134277})
store['active_learning_steps'][27]['eval_training']['best_epoch']=5
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 15521], ['id', 14540], ['id', 13760], ['id', 12934], ['id', 47599]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5937250444955304, 1.112576509517849, 1.5391488570519432, 1.8742687580346535, 2.0774850143302217]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9787813425064087})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6047863960266113})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5889362692832947})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5386708974838257})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5451035499572754})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5537790060043335})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.574219286441803})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6460012197494507})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5667142868041992})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.669452428817749})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5863262414932251})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6384815573692322})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5903291702270508})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5725321769714355})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6136729717254639})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6734044551849365})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6708713173866272})
store['active_learning_steps'][28]['training']['best_epoch']=14
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9315, 'crossentropy': 0.5724283203125}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.0165116786956787})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6246293783187866})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6075314283370972})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5280245542526245})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5421391129493713})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5357028245925903})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.48869842290878296})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.48587727546691895})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.49983417987823486})
store['active_learning_steps'][28]['eval_training']['best_epoch']=6
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 21012], ['id', 14852], ['id', 3961], ['id', 39604], ['id', 26765]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.7461686476699805, 1.3190144762607894, 1.8175657004522403, 2.2035008856391958, 2.4830137537592982]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.0526485443115234})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5746726989746094})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5682355165481567})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5297154188156128})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5161037445068359})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6069628596305847})
store['active_learning_steps'][29]['training']['best_epoch']=3
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9293, 'crossentropy': 0.4886546875}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.0589362382888794})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6482747793197632})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6056621074676514})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5464023947715759})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5123593211174011})
store['active_learning_steps'][29]['eval_training']['best_epoch']=4
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 52462], ['id', 33001], ['id', 13831], ['id', 45954], ['id', 57624]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6147962919777488, 1.1143134114374904, 1.5148656027943677, 1.803241059686397, 1.9899484848467246]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 0.9936386346817017})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6133212447166443})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5853501558303833})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.583376407623291})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6132891178131104})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.617628812789917})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5925211906433105})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.594578206539154})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6434365510940552})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5993725061416626})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6547744870185852})
store['active_learning_steps'][30]['training']['best_epoch']=8
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9275, 'crossentropy': 0.5358556640625}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.0364364385604858})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6179543137550354})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5863558053970337})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5207951664924622})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4800509810447693})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.48497286438941956})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4595198333263397})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.41962605714797974})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.4609469771385193})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.43210917711257935})
store['active_learning_steps'][30]['eval_training']['best_epoch']=10
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 13311], ['id', 8093], ['id', 23411], ['id', 59617], ['id', 7325]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7868618770356308, 1.397651452737211, 1.886432418804942, 2.277954058764832, 2.5734353203158085]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.0862542390823364})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6258129477500916})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5870165824890137})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5520861148834229})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5626410245895386})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5688160061836243})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5612560510635376})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.621841549873352})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5971370935440063})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5185415744781494})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5327789783477783})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6114163994789124})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5854659676551819})
store['active_learning_steps'][31]['training']['best_epoch']=10
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9342, 'crossentropy': 0.497512548828125}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.0040807723999023})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.6685700416564941})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6232578754425049})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5298133492469788})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4948248267173767})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.46887850761413574})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.493489146232605})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4597315192222595})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.47044211626052856})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.4910620450973511})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.4444804787635803})
store['active_learning_steps'][31]['eval_training']['best_epoch']=8
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 14428], ['id', 15579], ['id', 27179], ['id', 17478], ['id', 59544]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.7185008281090557, 1.2959615056544742, 1.8122886354734813, 2.184607640808333, 2.4586131382886727]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.0589377880096436})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6238805055618286})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5172758102416992})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5280393362045288})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.531179666519165})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.597642183303833})
store['active_learning_steps'][32]['training']['best_epoch']=3
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9283, 'crossentropy': 0.48857109375}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.0244168043136597})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6574092507362366})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5690802931785583})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5411273241043091})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5387898683547974})
store['active_learning_steps'][32]['eval_training']['best_epoch']=3
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 19188], ['id', 903], ['id', 8584], ['id', 25546], ['id', 51466]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5280046843954851, 1.0129200724280176, 1.406523207857541, 1.7164169865980838, 1.9350048051712943]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.0094274282455444})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6339370608329773})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5954940915107727})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5700072050094604})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5762207508087158})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6099907159805298})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6634931564331055})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6149318218231201})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.626592755317688})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6478757858276367})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.638943076133728})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6602267026901245})
store['active_learning_steps'][33]['training']['best_epoch']=9
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.927, 'crossentropy': 0.533270654296875}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.9750348329544067})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6547975540161133})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5430128574371338})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5194700956344604})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.49787139892578125})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4549916088581085})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4525379538536072})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4481663107872009})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.46316778659820557})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4195999503135681})
store['active_learning_steps'][33]['eval_training']['best_epoch']=7
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 41258], ['id', 55836], ['id', 34946], ['id', 55778], ['id', 3737]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6021313454599038, 1.1589020877655547, 1.6339902875724541, 1.9617078942526955, 2.1768872172252776]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.012312412261963})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.603126049041748})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5562433004379272})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5761533975601196})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6024118661880493})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5670425891876221})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5904816389083862})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6313723921775818})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.610579252243042})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.628869891166687})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6215735673904419})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6442687511444092})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6610727310180664})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6589274406433105})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6828567981719971})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6459845304489136})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6232832670211792})
store['active_learning_steps'][34]['training']['best_epoch']=14
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9249, 'crossentropy': 0.59486484375}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.0442538261413574})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5950563549995422})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.480995237827301})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.46505141258239746})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4442075788974762})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4513188302516937})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4511908292770386})
store['active_learning_steps'][34]['eval_training']['best_epoch']=4
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 31013], ['id', 14690], ['id', 140], ['id', 39683], ['id', 34676]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.7305984863820933, 1.3821453721680745, 1.8864706850963984, 2.2100798574323433, 2.3777286670507713]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.0233473777770996})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.659455418586731})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5934771299362183})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6122633218765259})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6330638527870178})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6923519372940063})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6503126621246338})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6640580296516418})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6932350397109985})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6508277654647827})
store['active_learning_steps'][35]['training']['best_epoch']=7
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9137, 'crossentropy': 0.58049326171875}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.1082875728607178})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6391220092773438})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.590234637260437})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5127219557762146})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5113892555236816})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.47886037826538086})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4608478546142578})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4707801342010498})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4445665180683136})
store['active_learning_steps'][35]['eval_training']['best_epoch']=7
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 18313], ['id', 18501], ['id', 25315], ['id', 49526], ['id', 11707]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7760684613656019, 1.3925291586434456, 1.8732837890418228, 2.2603564080211607, 2.543216288632136]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.0373605489730835})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6074398756027222})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5249727964401245})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5164077281951904})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5411331653594971})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5680422782897949})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5211516618728638})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5376695990562439})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5905218124389648})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6389833092689514})
store['active_learning_steps'][36]['training']['best_epoch']=7
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9358, 'crossentropy': 0.46328037109375}
