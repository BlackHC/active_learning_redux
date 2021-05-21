store = {}
store['timestamp']=1621481057
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=64']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=64
store['worker_id']=64
store['num_workers']=80
store['config']={'seed': 1302, 'uniform_ood': True, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('FastFashionMNIST Train (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 3792, 5573, 45567, 10508, 2728, 21423, 396, 49512, 31444]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.6156394481658936})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.8062710762023926})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.7217869758605957})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.7336835861206055})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.92624568939209})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.099008083343506})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.9332399368286133})
store['active_learning_steps'][0]['training']['best_epoch']=4
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.673, 'crossentropy': 2.634526953125}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.3652808666229248})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.42694091796875})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.5324410200119019})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.4605510234832764})
store['active_learning_steps'][0]['eval_training']['best_epoch']=1
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 9499], ['id', 41635], ['id', 59389], ['id', 56899], ['id', 1991]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.0535197375805927, 1.8056266481195427, 2.306105899083841, 2.659617157473253, 2.8514296306508546]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.540482997894287})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.8413432836532593})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.00592041015625})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.1526269912719727})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7179, 'crossentropy': 1.41175673828125}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.1685819625854492})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.1233391761779785})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.136213779449463})
store['active_learning_steps'][1]['eval_training']['best_epoch']=1
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 25711], ['id', 34678], ['id', 49291], ['id', 47344], ['id', 29880]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5865717890669211, 1.0668586583517845, 1.4244026010713862, 1.6907791233167977, 1.90051978283301]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.4902353286743164})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.8014881610870361})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.936149001121521})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.12627911567688})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.2058920860290527})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.2570929527282715})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.4716134071350098})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.32991099357605})
store['active_learning_steps'][2]['training']['best_epoch']=5
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7199, 'crossentropy': 1.963839453125}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.3251444101333618})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.3546292781829834})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.4187748432159424})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.376936912536621})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.4049878120422363})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.4225826263427734})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 41738], ['id', 2748], ['id', 1364], ['id', 51266], ['id', 58793]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7916337932971163, 1.4105444205103947, 1.9021201510051502, 2.312981697576898, 2.5906616490538434]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.5797631740570068})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.7096240520477295})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.8822993040084839})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.1307878494262695})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.2522826194763184})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.34085750579834})
store['active_learning_steps'][3]['training']['best_epoch']=3
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7175, 'crossentropy': 1.74106328125}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.4103248119354248})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.2503132820129395})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.3078782558441162})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.290013074874878})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.227125883102417})
store['active_learning_steps'][3]['eval_training']['best_epoch']=2
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 2810], ['id', 20426], ['id', 6297], ['id', 19638], ['id', 31946]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6538619823454872, 1.201888539833441, 1.6588156978908613, 1.9431157941330737, 2.140924929677551]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.2859978675842285})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.433960199356079})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.6511735916137695})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.6730389595031738})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7533, 'crossentropy': 1.1104150390625}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.1317627429962158})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.0720891952514648})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.0117865800857544})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 5062], ['id', 15005], ['id', 19406], ['id', 47635], ['id', 12254]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5657098097657429, 1.0203881967738528, 1.4245198514190625, 1.7537938712625492, 2.014361648209947]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.1802563667297363})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.3832323551177979})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.3574512004852295})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.5512278079986572})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.5598620176315308})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.6786199808120728})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.6687901020050049})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.704185962677002})
store['active_learning_steps'][5]['training']['best_epoch']=5
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7898, 'crossentropy': 1.35874208984375}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.158634066581726})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.1393625736236572})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.121782660484314})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.2599859237670898})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.166885256767273})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.2363145351409912})
store['active_learning_steps'][5]['eval_training']['best_epoch']=3
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 12986], ['id', 56155], ['id', 3031], ['id', 25747], ['id', 4820]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6680779552303845, 1.2469653810758337, 1.7115484141150006, 2.0702886839537857, 2.3434926871353343]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.3704535961151123})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.294237732887268})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.4497069120407104})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.5201101303100586})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.767653226852417})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.6682049036026})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.6762430667877197})
store['active_learning_steps'][6]['training']['best_epoch']=4
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7977, 'crossentropy': 1.2772103515625}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.3303093910217285})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.2698969841003418})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.2200171947479248})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.1587975025177002})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.1028873920440674})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.2394094467163086})
store['active_learning_steps'][6]['eval_training']['best_epoch']=5
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 7924], ['id', 40334], ['id', 18404], ['id', 15487], ['id', 50500]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6074214084924545, 1.0974775235662548, 1.5463364029327291, 1.8881134327761897, 2.132494462660051]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.2423738241195679})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.406404972076416})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.4886364936828613})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.5002808570861816})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.7879955768585205})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.7592767477035522})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.5133763551712036})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.7472140789031982})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.7943509817123413})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 2.093380928039551})
store['active_learning_steps'][7]['training']['best_epoch']=7
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.793, 'crossentropy': 1.41843212890625}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.2485191822052002})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.3084334135055542})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.3466792106628418})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.3455134630203247})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.2394578456878662})
store['active_learning_steps'][7]['eval_training']['best_epoch']=2
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 52934], ['id', 1260], ['id', 19129], ['id', 28787], ['id', 55102]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.5721018920481483, 1.1222674149608172, 1.5862322159739866, 1.916663538690825, 2.1689479640517697]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 0.9802170395851135})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.9715842008590698})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.0806591510772705})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.411715030670166})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.1274951696395874})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8493, 'crossentropy': 0.86033203125}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.0013399124145508})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 0.934842050075531})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 0.8515121936798096})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.8243227005004883})
store['active_learning_steps'][8]['eval_training']['best_epoch']=4
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 27423], ['id', 53170], ['id', 55639], ['id', 25960], ['id', 386]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5597149885475634, 1.051457338178524, 1.459655332128622, 1.7682436090226803, 1.989373521084648]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.0509942770004272})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.0651464462280273})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.1946611404418945})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.2504379749298096})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.3233277797698975})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.208225965499878})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.6328506469726562})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.4894100427627563})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.5754597187042236})
store['active_learning_steps'][9]['training']['best_epoch']=6
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8388, 'crossentropy': 1.1762482421875}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.1419639587402344})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.0746469497680664})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.0002923011779785})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.0660552978515625})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.0333642959594727})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.0352544784545898})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.9934288263320923})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.0139069557189941})
store['active_learning_steps'][9]['eval_training']['best_epoch']=5
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 2733], ['id', 17896], ['id', 41060], ['id', 52533], ['id', 41258]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7071378934288797, 1.2996725840600174, 1.7635602254078209, 2.118128818173747, 2.3766672754294578]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9586418867111206})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9272695779800415})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9686763286590576})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.0521156787872314})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.1919128894805908})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.1765341758728027})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.1014044284820557})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.0989762544631958})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.160121202468872})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.258368968963623})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.256685733795166})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.2635691165924072})
store['active_learning_steps'][10]['training']['best_epoch']=9
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8602, 'crossentropy': 1.10336123046875}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 0.9687565565109253})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 0.9725942611694336})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.973426103591919})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.9532033205032349})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9183677434921265})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.9643425941467285})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.9540258646011353})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.9366625547409058})
store['active_learning_steps'][10]['eval_training']['best_epoch']=5
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 59339], ['id', 37154], ['id', 46088], ['id', 23388], ['id', 17521]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8049127055168479, 1.5468593336198964, 2.1010982498187185, 2.4318584908517, 2.6575157447131934]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8642525672912598})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8548889756202698})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8319021463394165})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8314422369003296})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.9851632118225098})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9894725680351257})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9560447931289673})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.126267433166504})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.123220682144165})
store['active_learning_steps'][11]['training']['best_epoch']=6
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8781, 'crossentropy': 0.89184580078125}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.9187424778938293})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8413265943527222})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7726502418518066})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6980202198028564})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.687445878982544})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7548447847366333})
store['active_learning_steps'][11]['eval_training']['best_epoch']=3
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 14205], ['id', 20855], ['id', 5013], ['id', 25187], ['id', 46815]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6934853945854409, 1.3075527381519154, 1.8374898264897237, 2.195635587396371, 2.4832729241980456]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 0.9592550992965698})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8386790752410889})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8938849568367004})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.9413001537322998})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.9426363706588745})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.9288809299468994})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.1018579006195068})
store['active_learning_steps'][12]['training']['best_epoch']=4
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8546, 'crossentropy': 0.89470234375}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.0018353462219238})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.7640371322631836})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6885144710540771})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6841697096824646})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7087061405181885})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.6851702928543091})
store['active_learning_steps'][12]['eval_training']['best_epoch']=3
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 1143], ['id', 51502], ['id', 28351], ['id', 34802], ['id', 1414]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.677030806622695, 1.2876156038058295, 1.6926298490188674, 2.0041317394662204, 2.1906566572145456]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.9658597707748413})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8695948123931885})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8790534734725952})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9306720495223999})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9407696723937988})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.0254828929901123})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8706, 'crossentropy': 0.8083703125}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.922294020652771})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8216880559921265})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.7677067518234253})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.7450920343399048})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.6947598457336426})
store['active_learning_steps'][13]['eval_training']['best_epoch']=5
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 49905], ['id', 26504], ['id', 13705], ['id', 19855], ['id', 55116]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7314224089073897, 1.3830786148900014, 1.859472155266082, 2.236538129410254, 2.51444938616884]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 0.9697184562683105})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.9321537017822266})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.0361790657043457})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.1090657711029053})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.0487453937530518})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.0859034061431885})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.2452287673950195})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.156307578086853})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.3338779211044312})
store['active_learning_steps'][14]['training']['best_epoch']=6
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8666, 'crossentropy': 0.95977265625}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.091036081314087})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8771755695343018})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.8871363401412964})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.8170807361602783})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8538544178009033})
store['active_learning_steps'][14]['eval_training']['best_epoch']=2
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 41044], ['id', 9180], ['id', 52896], ['id', 51492], ['id', 32538]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.6796216617698705, 1.2301266052528845, 1.6556569702971964, 1.965187272764204, 2.1702289194334097]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.068181037902832})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9126943945884705})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.957945704460144})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.9851400256156921})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.0335458517074585})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.0967859029769897})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.2000430822372437})
store['active_learning_steps'][15]['training']['best_epoch']=4
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8726, 'crossentropy': 0.812178466796875}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 0.9522862434387207})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.8289637565612793})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.7631687521934509})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.6934463977813721})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.7428311705589294})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.7092488408088684})
store['active_learning_steps'][15]['eval_training']['best_epoch']=4
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 424], ['id', 20448], ['id', 36760], ['id', 37584], ['id', 44446]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5677822199322728, 1.0874514501065216, 1.5387042509038964, 1.8969394896391218, 2.1469506163663903]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.0654267072677612})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.8616248965263367})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9231181144714355})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.95668625831604})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.9641591310501099})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.1066386699676514})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.1856753826141357})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.2588809728622437})
store['active_learning_steps'][16]['training']['best_epoch']=5
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8556, 'crossentropy': 0.87741904296875}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.0400843620300293})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.8854137659072876})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.7722784876823425})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.8574048280715942})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.8098740577697754})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.7673623561859131})
store['active_learning_steps'][16]['eval_training']['best_epoch']=3
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 27153], ['id', 5600], ['id', 13096], ['id', 16170], ['id', 38365]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.535588320882007, 1.0353871141860354, 1.427053340337598, 1.6994201034495449, 1.894205891890862]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.946542501449585})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8298187851905823})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8806939721107483})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.0648002624511719})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.112082600593567})
store['active_learning_steps'][17]['training']['best_epoch']=2
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8666, 'crossentropy': 0.739779638671875}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.9264332056045532})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.7666858434677124})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.6850054264068604})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.7068407535552979})
store['active_learning_steps'][17]['eval_training']['best_epoch']=3
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 44998], ['id', 26843], ['id', 45026], ['id', 55539], ['id', 826]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.5476051584080937, 1.0383203176971842, 1.4354032781155843, 1.7454087185465461, 1.9760075304010405]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.929201602935791})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8709341883659363})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.9165793657302856})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.9063302278518677})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8982274532318115})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.9721845388412476})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.0257139205932617})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.092475414276123})
store['active_learning_steps'][18]['training']['best_epoch']=5
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8759, 'crossentropy': 0.8037205078125}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.9054499268531799})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7447026371955872})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.7473732233047485})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.6779953241348267})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.6794661283493042})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.715268611907959})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.6977853775024414})
store['active_learning_steps'][18]['eval_training']['best_epoch']=4
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 46068], ['id', 35692], ['id', 49624], ['id', 4502], ['id', 23109]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5969261091443646, 1.11669644389619, 1.5560713161051807, 1.9090743878478906, 2.206380716164489]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.9187283515930176})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.8411893844604492})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.9150667786598206})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9163470268249512})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.2629761695861816})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.9897755980491638})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.2297970056533813})
store['active_learning_steps'][19]['training']['best_epoch']=4
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8645, 'crossentropy': 0.803034228515625}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.9057919383049011})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.7502014636993408})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.7957900762557983})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.7554193735122681})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.7214916348457336})
store['active_learning_steps'][19]['eval_training']['best_epoch']=2
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 28632], ['id', 5325], ['id', 11044], ['id', 5474], ['id', 24894]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.602086646850389, 1.10447033476476, 1.5301174998476084, 1.8851836033065434, 2.1466485965822604]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.9446836113929749})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8506603240966797})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7894077301025391})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.9461669325828552})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8798521757125854})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.9603163003921509})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9718223810195923})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.0740878582000732})
store['active_learning_steps'][20]['training']['best_epoch']=5
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8853, 'crossentropy': 0.78758837890625}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9087941646575928})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.7678093314170837})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.6770219802856445})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.6676380634307861})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.684607744216919})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.6585395932197571})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.6725893020629883})
store['active_learning_steps'][20]['eval_training']['best_epoch']=4
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 50806], ['id', 17239], ['id', 22364], ['id', 1075], ['id', 17539]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6574640875022826, 1.2218193711762906, 1.6951500763209433, 2.042301113243779, 2.273847360807089]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.990456759929657})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8343784809112549})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7291418313980103})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.79566890001297})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8775657415390015})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8705805540084839})
store['active_learning_steps'][21]['training']['best_epoch']=3
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.885, 'crossentropy': 0.653743115234375}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.8792529106140137})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.7176036834716797})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.6541883945465088})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.6385747194290161})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.6062790751457214})
store['active_learning_steps'][21]['eval_training']['best_epoch']=5
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 19981], ['id', 49107], ['id', 12297], ['id', 34268], ['id', 4116]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.6287487929101392, 1.1748594487623838, 1.6307072444425126, 1.9730267328629658, 2.2030759995474565]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.9681965112686157})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.9019128084182739})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.9125421047210693})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.0094962120056152})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.9972638487815857})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.981520414352417})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.056541919708252})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.1327351331710815})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.3330026865005493})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.04872727394104})
store['active_learning_steps'][22]['training']['best_epoch']=7
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8727, 'crossentropy': 0.891815625}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 0.9885659217834473})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7048613429069519})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.721316933631897})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.690564751625061})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.6714107990264893})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.6562194228172302})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.6601518392562866})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.6267995834350586})
store['active_learning_steps'][22]['eval_training']['best_epoch']=5
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 43711], ['id', 34665], ['id', 50317], ['id', 22480], ['id', 52727]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6826520280318361, 1.3031312033320108, 1.8144105555505639, 2.19222689842619, 2.3887424648470184]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.9364028573036194})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7525754570960999})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8007330298423767})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8223373889923096})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8113300800323486})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.9289159774780273})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.004662036895752})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9537175893783569})
store['active_learning_steps'][23]['training']['best_epoch']=5
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9027, 'crossentropy': 0.681680712890625}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 0.9347299337387085})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.7778098583221436})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.6949174404144287})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.7186670303344727})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.6645969748497009})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6067852973937988})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.601603627204895})
store['active_learning_steps'][23]['eval_training']['best_epoch']=6
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 46316], ['id', 39451], ['id', 35606], ['id', 20050], ['id', 32137]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6789496282200775, 1.3114663353078764, 1.801935252421873, 2.0914566460083144, 2.2800260675205966]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9774478673934937})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8352363109588623})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8399984836578369})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7432587146759033})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8149228692054749})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9231866598129272})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8602020740509033})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9012, 'crossentropy': 0.627856005859375}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.9285136461257935})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6659466028213501})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6460672616958618})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6179251670837402})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.5470016002655029})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.5646752715110779})
store['active_learning_steps'][24]['eval_training']['best_epoch']=5
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 23104], ['id', 44753], ['id', 32510], ['id', 34188], ['id', 43434]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6112335539107032, 1.1114776593154683, 1.495142514292814, 1.7552976556528526, 1.9469249917142992]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.0517375469207764})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7207982540130615})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6955398321151733})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7858612537384033})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7255412936210632})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8017920255661011})
store['active_learning_steps'][25]['training']['best_epoch']=3
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.899, 'crossentropy': 0.608971826171875}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.9710149168968201})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7065432071685791})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6692475080490112})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6366671323776245})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.550297737121582})
store['active_learning_steps'][25]['eval_training']['best_epoch']=5
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 29410], ['id', 47260], ['id', 42415], ['id', 43059], ['id', 27930]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.682282708242983, 1.2362410385713227, 1.6603345700866932, 1.9841083695928763, 2.1935923099489365]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.9507024884223938})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.668460488319397})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6724419593811035})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7298572063446045})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7642861008644104})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7973936796188354})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8213164806365967})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7914365530014038})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8760327696800232})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.8548293709754944})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8431594967842102})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8038811683654785})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8439472913742065})
store['active_learning_steps'][26]['training']['best_epoch']=10
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9048, 'crossentropy': 0.735667041015625}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8963220119476318})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6947566866874695})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6246822476387024})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6257480382919312})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6505861282348633})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6020123958587646})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6286460161209106})
store['active_learning_steps'][26]['eval_training']['best_epoch']=4
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 30688], ['id', 57231], ['id', 45414], ['id', 11336], ['id', 20614]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6459605355154452, 1.1812685620352075, 1.6348809107710158, 1.982755110880341, 2.1962937180278477]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.9200047254562378})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7067378759384155})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7091184854507446})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6831880807876587})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7575218677520752})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7679846286773682})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7390719056129456})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8436285853385925})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8643869161605835})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.9275479316711426})
store['active_learning_steps'][27]['training']['best_epoch']=7
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9146, 'crossentropy': 0.60735537109375}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.01546049118042})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7492678165435791})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6234556436538696})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.5924280881881714})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5551724433898926})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5682060718536377})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.5558153390884399})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.5220268964767456})
store['active_learning_steps'][27]['eval_training']['best_epoch']=5
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 45212], ['id', 41133], ['id', 16022], ['id', 36562], ['id', 21614]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6657608812845569, 1.2812317923358103, 1.7737028334316767, 2.1086930484553035, 2.2898572316014256]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.900061845779419})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6616998910903931})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6772128939628601})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6688246726989746})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7265172004699707})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7368558645248413})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7505381107330322})
store['active_learning_steps'][28]['training']['best_epoch']=4
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9111, 'crossentropy': 0.597920458984375}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 0.960606575012207})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6116228103637695})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5915381908416748})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5435073375701904})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5231779217720032})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.560348629951477})
store['active_learning_steps'][28]['eval_training']['best_epoch']=4
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 14765], ['id', 28357], ['id', 57728], ['id', 20337], ['id', 26956]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6120164763127649, 1.1071412795317772, 1.533887681969083, 1.8206931481837945, 2.0210756616630654]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.9281683564186096})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6589992046356201})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6364624500274658})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6945430040359497})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6800212860107422})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7010532021522522})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6823776960372925})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7295933961868286})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.731849193572998})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7587885856628418})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7678437232971191})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7820433378219604})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8881418704986572})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.8003970384597778})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.9139364957809448})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8595402240753174})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.9090666174888611})
store['active_learning_steps'][29]['training']['best_epoch']=14
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9215, 'crossentropy': 0.664394580078125}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 0.9734557867050171})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7325466871261597})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6548411846160889})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6117645502090454})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5959860682487488})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6222634315490723})
store['active_learning_steps'][29]['eval_training']['best_epoch']=3
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 43897], ['id', 59651], ['id', 46435], ['id', 37440], ['id', 5687]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6687313474913206, 1.268805200608928, 1.7436251355081644, 2.1371860546336388, 2.413024783662316]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.983018696308136})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6380815505981445})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.605288028717041})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.601061224937439})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6264872550964355})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5776455998420715})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7223570346832275})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6567760705947876})
store['active_learning_steps'][30]['training']['best_epoch']=5
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9272, 'crossentropy': 0.508829541015625}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.9214102029800415})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6165156364440918})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.56273353099823})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.54808509349823})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5058319568634033})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.49385714530944824})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.49807506799697876})
store['active_learning_steps'][30]['eval_training']['best_epoch']=6
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 24601], ['id', 12066], ['id', 43212], ['id', 7574], ['id', 22029]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.6163293442313555, 1.159450296673147, 1.6035042955614083, 1.9327077989246648, 2.1674852838725815]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.0071710348129272})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6776396036148071})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6551110744476318})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6780476570129395})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7160089015960693})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7870086431503296})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7201516628265381})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8098957538604736})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7518340945243835})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8333351612091064})
store['active_learning_steps'][31]['training']['best_epoch']=7
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9198, 'crossentropy': 0.617990869140625}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.026498794555664})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7300623059272766})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6567885875701904})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5519884824752808})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5700160264968872})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5771076679229736})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5177222490310669})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5135253667831421})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5066510438919067})
store['active_learning_steps'][31]['eval_training']['best_epoch']=8
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 5626], ['id', 8097], ['id', 34558], ['id', 54671], ['id', 45109]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6460432723288163, 1.2212863898340194, 1.7106899368571644, 2.0904762603634115, 2.3845548540825647]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.1123902797698975})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.644950270652771})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5895295739173889})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.606295108795166})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6260626912117004})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.668393611907959})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6519443988800049})
store['active_learning_steps'][32]['training']['best_epoch']=4
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.926, 'crossentropy': 0.50510771484375}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.975375771522522})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6226171255111694})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5379959344863892})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5186208486557007})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.48228418827056885})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.49154743552207947})
store['active_learning_steps'][32]['eval_training']['best_epoch']=6
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 50576], ['id', 47387], ['id', 10028], ['id', 8447], ['id', 12934]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6500631066298554, 1.203442425421819, 1.6450186477696516, 1.9872346621541803, 2.1958761091095536]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.9532119631767273})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6443490982055664})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5454064607620239})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5665693283081055})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5478386878967285})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6056618690490723})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6673038005828857})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6191424131393433})
store['active_learning_steps'][33]['training']['best_epoch']=5
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9318, 'crossentropy': 0.5117935546875}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9387204647064209})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6289634704589844})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5614778995513916})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5146927833557129})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.48369306325912476})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.46229586005210876})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4816872775554657})
store['active_learning_steps'][33]['eval_training']['best_epoch']=7
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 38050], ['id', 44570], ['id', 36990], ['id', 48540], ['id', 11208]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.7027617281152365, 1.3061418061615084, 1.7837796883794086, 2.147959445656319, 2.3655656753025296]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.0263826847076416})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6609238386154175})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5851441621780396})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6091564893722534})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5964150428771973})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6618655920028687})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6547805070877075})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6705842018127441})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6756221055984497})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.64780193567276})
store['active_learning_steps'][34]['training']['best_epoch']=7
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9272, 'crossentropy': 0.554090234375}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.000819444656372})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6032392978668213})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5456770658493042})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5066510438919067})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5002270340919495})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4759314954280853})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4499198794364929})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4638795256614685})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4541630148887634})
store['active_learning_steps'][34]['eval_training']['best_epoch']=7
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 7995], ['id', 27733], ['id', 49029], ['id', 56457], ['id', 35652]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6768647773908016, 1.2531831419975248, 1.7321861836872765, 2.0744996429281404, 2.3060007331292276]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.959003210067749})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6516828536987305})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5081796646118164})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5366787910461426})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5429410338401794})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5495401620864868})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.582586407661438})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5970392227172852})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6955646276473999})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6232004165649414})
store['active_learning_steps'][35]['training']['best_epoch']=7
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9346, 'crossentropy': 0.495307421875}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9874846935272217})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6441714763641357})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5297836661338806})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5006862878799438})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4557974934577942})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4515233635902405})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4572560787200928})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4148261547088623})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4415798783302307})
store['active_learning_steps'][35]['eval_training']['best_epoch']=8
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 12524], ['id', 37688], ['id', 16961], ['id', 56224], ['id', 59363]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.6149079820139634, 1.145323103517382, 1.6008337908834083, 1.9061649230679496, 2.1351346577675097]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.1177653074264526})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6016278266906738})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5854346752166748})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5602012872695923})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.552043616771698})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6345783472061157})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6207062005996704})
store['active_learning_steps'][36]['training']['best_epoch']=4
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9328, 'crossentropy': 0.46913076171875}
