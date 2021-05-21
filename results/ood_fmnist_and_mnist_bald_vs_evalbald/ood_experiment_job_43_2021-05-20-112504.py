store = {}
store['timestamp']=1621506304
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=43']
store['commit']='35841c01d6111c8009c59adebde0572fb40fe6d5'
store['github_url']='35841c01d6111c8009c59adebde0572fb40fe6d5'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=43
store['worker_id']=43
store['num_workers']=80
store['config']={'seed': 1279, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples)) + ('FastMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 14640, 45567, 52801, 53689, 801, 55187, 26479, 50997, 3792]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.597627639770508})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.161630392074585})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.6348166465759277})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.622145891189575})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.5921, 'crossentropy': 2.68907265625}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 8570], ['id', 29088], ['id', 37777], ['id', 25994], ['id', 54092]], 'labels': [-1, 8, -1, -1, -1], 'scores': [1.410237203848034, 2.461793936442926, 3.2494363160482607, 3.7975457562308073, 4.13249610139855]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.429123878479004})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.1015329360961914})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.0575318336486816})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.049572706222534})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.064305305480957})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.247633934020996})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.6359193325042725})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.1162772178649902})
store['active_learning_steps'][1]['training']['best_epoch']=5
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6192, 'crossentropy': 3.468839453125}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 38079], ['id', 25210], ['id', 50294], ['id', 56526], ['id', 926]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4725811643925633, 2.7042592086378807, 3.5688601689985067, 4.084233550258191, 4.3565704222590576]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 2.7258100509643555})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 3.6200737953186035})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.7855825424194336})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 3.9284651279449463})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5703125, 'crossentropy': 4.4535675048828125})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 3.8352537155151367})
store['active_learning_steps'][2]['training']['best_epoch']=3
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.5755, 'crossentropy': 3.9730359375}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 54171], ['id', 47444], ['id', 55739], ['id', 46594], ['id', 32411]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6105500822733712, 2.7441408069336246, 3.6087778993809643, 4.100207306794493, 4.375285378985859]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 2.6523759365081787})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 3.369417667388916})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 3.6154911518096924})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5751953125, 'crossentropy': 3.8314857482910156})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.554, 'crossentropy': 2.8631783203125}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 12207], ['id', 28517], ['id', 40390], ['id', 39461], ['id', 49138]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2779444567590703, 2.3958394175424207, 3.1372556074871483, 3.6793072053994162, 4.028096616967204]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5693359375, 'crossentropy': 2.7425308227539062})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 4.030041694641113})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5703125, 'crossentropy': 4.341886043548584})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5634765625, 'crossentropy': 4.314460754394531})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 4.423052787780762})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 4.62095832824707})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 4.276593208312988})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 4.941559791564941})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 4.333810806274414})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 4.446949005126953})
store['active_learning_steps'][4]['training']['best_epoch']=7
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.5862, 'crossentropy': 4.69158203125}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 21935], ['id', 49115], ['id', 47220], ['id', 1958], ['id', 19505]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5817707351590569, 2.725318098903683, 3.568089566207502, 4.066891689564123, 4.346199825659237]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.4428648948669434})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.3288140296936035})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.1689412593841553})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.459453821182251})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 4.245534420013428})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.680473566055298})
store['active_learning_steps'][5]['training']['best_epoch']=3
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.5969, 'crossentropy': 3.3358015625}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 32504], ['id', 57538], ['id', 23020], ['id', 51006], ['id', 31779]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5644622723011483, 2.7092497859384905, 3.6016274870204468, 4.128967550125547, 4.3784520079536335]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 2.405088424682617})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.8728585243225098})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.436532497406006})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.1175501346588135})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.7785322666168213})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.6666245460510254})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.503678321838379})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.6236977577209473})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.3024916648864746})
store['active_learning_steps'][6]['training']['best_epoch']=6
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.5931, 'crossentropy': 3.920767578125}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 21875], ['id', 39451], ['id', 44993], ['id', 20124], ['id', 25572]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4832365088029842, 2.7032021582249333, 3.6203825213896925, 4.144101066239854, 4.389099682259755]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.489147424697876})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.6274938583374023})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 2.959322452545166})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.2103333473205566})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.5882, 'crossentropy': 2.570811328125}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 19697], ['id', 45048], ['id', 59408], ['id', 41985], ['id', 32776]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3814821705058742, 2.5236829759447836, 3.2996808769578347, 3.8244958635387647, 4.134798088883615]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.568359375, 'crossentropy': 2.7384982109069824})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.975111484527588})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.5339579582214355})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.3674516677856445})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 3.4216651916503906})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.5899, 'crossentropy': 3.340541015625}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 56094], ['id', 33289], ['id', 35397], ['id', 45760], ['id', 59390]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6420999058295864, 2.8017220400674887, 3.590824529768959, 4.091174991834867, 4.351283608937248]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 2.4715495109558105})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 3.114471197128296})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.1122565269470215})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.0094361305236816})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.825727701187134})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.6145548820495605})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.907731771469116})
store['active_learning_steps'][9]['training']['best_epoch']=4
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.5921, 'crossentropy': 3.531712109375}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 8677], ['id', 49850], ['id', 48926], ['id', 24030], ['id', 32383]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.520351331422182, 2.7723914237327287, 3.6920709338291733, 4.207016683136694, 4.426526716082531]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.4936447143554688})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.0948429107666016})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.606618881225586})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.490666389465332})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.5872, 'crossentropy': 2.4717923828125}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 15927], ['id', 50294], ['id', 34586], ['id', 21797], ['id', 32393]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.442314308528966, 2.4728034904925327, 3.223379293173215, 3.7324937383884897, 4.0589300142844476]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 2.772796630859375})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.091064453125})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.799323558807373})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.675126075744629})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 4.285240173339844})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.9737110137939453})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.983484983444214})
store['active_learning_steps'][11]['training']['best_epoch']=4
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.5946, 'crossentropy': 3.947283984375}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 54588], ['id', 14335], ['id', 27181], ['id', 52942], ['id', 17728]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5832329040666764, 2.7204516401966057, 3.5348885344948124, 4.031511710428849, 4.300222029026642]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 2.3920698165893555})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.176058053970337})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 3.1979641914367676})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 4.224636077880859})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 4.04080867767334})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.5716, 'crossentropy': 3.389883203125}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 9937], ['id', 17332], ['id', 27765], ['id', 24063], ['id', 16911]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4892024212171926, 2.7443577103254393, 3.5907494287258954, 4.088149706647174, 4.354527671801807]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.576171875, 'crossentropy': 2.715402603149414})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 3.448913097381592})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 4.182523727416992})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 4.340174674987793})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 4.548002243041992})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.6814632415771484})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 4.325066089630127})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 4.318533897399902})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 4.051250457763672})
store['active_learning_steps'][13]['training']['best_epoch']=6
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.5792, 'crossentropy': 3.951309765625}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 38568], ['id', 34916], ['id', 52719], ['id', 5151], ['id', 4905]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6035112982586224, 2.832998760097939, 3.6909930560441477, 4.170069868180425, 4.393790946144543]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5615234375, 'crossentropy': 2.411008358001709})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 3.1160888671875})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 3.202604293823242})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.564453125, 'crossentropy': 3.7881860733032227})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 4.124449729919434})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 4.051321029663086})
store['active_learning_steps'][14]['training']['best_epoch']=3
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.5647, 'crossentropy': 3.454159765625}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 49418], ['id', 45873], ['id', 56561], ['id', 15795], ['id', 13952]], 'labels': [-1, -1, 2, -1, -1], 'scores': [1.5468797101563148, 2.738974778266242, 3.6033353800074623, 4.135866529872596, 4.411345727468779]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 2.6862149238586426})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.5791015625, 'crossentropy': 3.511434316635132})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.6026177406311035})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.762704372406006})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 4.197884559631348})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 3.964357376098633})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 4.182506561279297})
store['active_learning_steps'][15]['training']['best_epoch']=4
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.5817, 'crossentropy': 4.279778515625}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 32504], ['id', 57300], ['id', 50456], ['id', 59417], ['id', 6081]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6269274569200785, 2.795852249030787, 3.6447131028109556, 4.121335070497593, 4.370404270051719]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 2.2971301078796387})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 3.1208348274230957})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.712491512298584})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.467416286468506})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 4.004968643188477})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.9041924476623535})
store['active_learning_steps'][16]['training']['best_epoch']=3
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.5834, 'crossentropy': 3.97380859375}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 26456], ['id', 28126], ['id', 23510], ['id', 50052], ['id', 32329]], 'labels': [-1, -1, 1, -1, -1], 'scores': [1.384230060021808, 2.5334588006069367, 3.371331650443203, 3.912852800182539, 4.240909358176076]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 2.527876377105713})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.2429699897766113})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.7151641845703125})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.7164740562438965})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.636295795440674})
store['active_learning_steps'][17]['training']['best_epoch']=2
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.5994, 'crossentropy': 3.4458921875}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 21797], ['id', 49286], ['id', 49850], ['id', 2986], ['id', 35930]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5389102376203367, 2.726958256071111, 3.525357413206173, 4.040648522344283, 4.324121054760731]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.4476661682128906})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.126363754272461})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.355551242828369})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.8154311180114746})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.2402992248535156})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.805058240890503})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.479330062866211})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 4.192262649536133})
store['active_learning_steps'][18]['training']['best_epoch']=5
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.5911, 'crossentropy': 3.850153515625}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 42714], ['id', 32583], ['id', 18564], ['id', 1253], ['id', 54737]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5818018522891402, 2.806520822857775, 3.643227476179246, 4.168768265134047, 4.407137493661068]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 2.5070743560791016})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.0229573249816895})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.365750312805176})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.4611034393310547})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.5739235877990723})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.6942105293273926})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.5762453079223633})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.7283740043640137})
store['active_learning_steps'][19]['training']['best_epoch']=5
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.5972, 'crossentropy': 3.79531875}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 30180], ['id', 38539], ['id', 32504], ['id', 15831], ['id', 34213]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.568137752266733, 2.746409745407979, 3.5849091564731363, 4.110279949886895, 4.3624687090180245]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.5712890625, 'crossentropy': 2.704888105392456})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 3.329831123352051})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.576171875, 'crossentropy': 3.6392836570739746})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 4.13196325302124})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 4.3353753089904785})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 4.600802421569824})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 4.314039707183838})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 4.776952743530273})
store['active_learning_steps'][20]['training']['best_epoch']=5
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.5748, 'crossentropy': 4.64784140625}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 42684], ['id', 35351], ['id', 50052], ['id', 54288], ['id', 1363]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5667144650348672, 2.8147762509201746, 3.6747989885945227, 4.160519232890417, 4.408008785031599]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 2.40098237991333})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.3717150688171387})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 3.95919132232666})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.7688446044921875})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 4.021393775939941})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 4.303450107574463})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 4.537066459655762})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 4.454955101013184})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 4.307812690734863})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 4.433967590332031})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 4.238726615905762})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 4.0327911376953125})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 5.075039863586426})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 4.3722686767578125})
store['active_learning_steps'][21]['training']['best_epoch']=11
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.601, 'crossentropy': 4.466659375}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 55575], ['id', 22531], ['id', 6088], ['id', 13455], ['id', 30582]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6495361504296002, 3.005999058086874, 3.888997825142898, 4.305572291888861, 4.4834256991951404]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.5722923278808594})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.840174674987793})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.1941161155700684})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.554185152053833})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.4392142295837402})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.537759304046631})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.3366856575012207})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 4.186821937561035})
store['active_learning_steps'][22]['training']['best_epoch']=5
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.6085, 'crossentropy': 3.541058203125}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 164], ['id', 11005], ['id', 34890], ['id', 44471], ['id', 36810]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.7451508744452982, 2.987719586824941, 3.7363746427212785, 4.171801000148262, 4.414925356985709]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.55859375, 'crossentropy': 2.960549831390381})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 3.519350528717041})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 3.461217164993286})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 4.0661516189575195})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 3.83404541015625})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 3.868697166442871})
store['active_learning_steps'][23]['training']['best_epoch']=3
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.5791, 'crossentropy': 3.73767890625}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 21931], ['id', 21880], ['id', 57184], ['id', 39437], ['id', 39510]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3925629643323036, 2.455343518431565, 3.253365198770119, 3.8441286942129675, 4.19735072377381]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.548828125, 'crossentropy': 2.682880163192749})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.3767547607421875})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 3.6213622093200684})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 3.9784371852874756})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.613034725189209})
store['active_learning_steps'][24]['training']['best_epoch']=2
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.5789, 'crossentropy': 3.388098828125}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 40164], ['id', 11446], ['id', 44496], ['id', 58235], ['id', 24437]], 'labels': [-1, 5, -1, -1, -1], 'scores': [1.4420881983220593, 2.540112874381057, 3.331317389445873, 3.8418291406947302, 4.152502818754124]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 2.4633679389953613})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.0118894577026367})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.7037882804870605})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 4.125842094421387})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.86891508102417})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.95418381690979})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 4.072909355163574})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.950145721435547})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 4.286925792694092})
store['active_learning_steps'][25]['training']['best_epoch']=6
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.5884, 'crossentropy': 4.3730203125}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 56094], ['id', 44535], ['id', 36152], ['id', 30266], ['id', 9131]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6682365565142128, 2.914654117236167, 3.760773337247276, 4.205075705655462, 4.4470249086388645]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.3624765872955322})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.809206485748291})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.490666627883911})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.441530704498291})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.7775423526763916})
store['active_learning_steps'][26]['training']['best_epoch']=2
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.6123, 'crossentropy': 2.9421919921875}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 164], ['id', 32504], ['id', 18564], ['id', 35930], ['id', 47260]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6128495758567718, 2.7134546318894044, 3.480132223758332, 4.001728011046458, 4.30741900202152]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.122730016708374})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.578808546066284})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.769482135772705})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.718931198120117})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.7250959873199463})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.357609272003174})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.0699825286865234})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.410926342010498})
store['active_learning_steps'][27]['training']['best_epoch']=5
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.6241, 'crossentropy': 3.25830390625}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 17510], ['id', 47375], ['id', 36427], ['id', 45404], ['id', 37994]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6435089517742267, 2.859516508021119, 3.7114160369687834, 4.187139931357507, 4.417881503079552]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 2.435127019882202})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.746196746826172})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.201772928237915})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.2929883003234863})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.9355931282043457})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.680532932281494})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.838397741317749})
store['active_learning_steps'][28]['training']['best_epoch']=4
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.6003, 'crossentropy': 3.711225390625}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 11226], ['id', 33964], ['id', 4833], ['id', 32504], ['id', 125]], 'labels': [-1, -1, -1, -1, 2], 'scores': [1.7019171867806255, 2.973113963010446, 3.805462472860472, 4.243084899098475, 4.443151900485663]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.1001462936401367})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.873584270477295})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 3.37976336479187})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 3.454861640930176})
store['active_learning_steps'][29]['training']['best_epoch']=1
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.599, 'crossentropy': 2.3353025390625}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 49418], ['id', 52224], ['id', 15927], ['id', 25218], ['id', 48463]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3782697054452542, 2.393408996010358, 3.10336957313978, 3.6157811186738478, 3.9696481884351034]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 2.590315818786621})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.1708812713623047})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.495572566986084})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.716538906097412})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.6356208324432373})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.769394874572754})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 4.173541069030762})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.8154664039611816})
store['active_learning_steps'][30]['training']['best_epoch']=5
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.5925, 'crossentropy': 4.205310546875}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 6238], ['id', 55519], ['id', 1865], ['id', 7649], ['id', 21290]], 'labels': [-1, -1, -1, -1, 3], 'scores': [1.6062754265844765, 2.785551490621774, 3.6289176854987835, 4.152833025117598, 4.393157360534781]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.572265625, 'crossentropy': 2.457516670227051})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 2.771977186203003})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.9308388233184814})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.9833364486694336})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.4952306747436523})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.435335397720337})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.790510654449463})
store['active_learning_steps'][31]['training']['best_epoch']=4
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.6069, 'crossentropy': 3.31404140625}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 21140], ['id', 35791], ['id', 26979], ['id', 36134], ['id', 5982]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6272667907339122, 2.8195383908405343, 3.6415905471929237, 4.157184843313885, 4.391088208352803]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.57421875, 'crossentropy': 2.2582411766052246})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 2.9845457077026367})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.147059917449951})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.5704493522644043})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 3.719449996948242})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.47163987159729})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.6417880058288574})
store['active_learning_steps'][32]['training']['best_epoch']=4
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.5959, 'crossentropy': 3.51518125}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 17870], ['id', 30469], ['id', 21348], ['id', 22620], ['id', 1682]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5332499865075095, 2.7948949389738287, 3.658041134928319, 4.148586409708507, 4.398362248724981]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.2406535148620605})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.50089168548584})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.659722328186035})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.2681527137756348})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.247115135192871})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.4811277389526367})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.3919119834899902})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.619621753692627})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.318939685821533})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.8593151569366455})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.818416118621826})
store['active_learning_steps'][33]['training']['best_epoch']=8
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.6183, 'crossentropy': 3.816749609375}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 59451], ['id', 30341], ['id', 36323], ['id', 9725], ['id', 8704]], 'labels': [-1, -1, 0, -1, -1], 'scores': [1.6937471695007298, 2.94020095580162, 3.785424860772202, 4.24194603941074, 4.472121734999158]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.042182207107544})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.6807260513305664})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.1052756309509277})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.1925573348999023})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.0750226974487305})
store['active_learning_steps'][34]['training']['best_epoch']=2
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.6103, 'crossentropy': 2.8068833984375}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 164], ['id', 46445], ['id', 34654], ['id', 32976], ['id', 41301]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.517751218850174, 2.735863906515114, 3.6156271442381653, 4.090981249896959, 4.360777862837587]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.0689008235931396})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.56046199798584})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.0242042541503906})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.2696523666381836})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.540104866027832})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.4725589752197266})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.6863791942596436})
store['active_learning_steps'][35]['training']['best_epoch']=4
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.6154, 'crossentropy': 3.33197890625}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 9069], ['id', 4829], ['id', 2935], ['id', 44746], ['id', 22577]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5761187214583006, 2.956504170482737, 3.750603637259756, 4.194541227093802, 4.414102565768611]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.2730352878570557})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.9376206398010254})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.243936061859131})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.9653844833374023})
store['active_learning_steps'][36]['training']['best_epoch']=1
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.5935, 'crossentropy': 2.32171484375}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 2962], ['id', 30266], ['id', 4618], ['id', 18497], ['id', 42821]], 'labels': [-1, -1, 2, -1, -1], 'scores': [1.3406888710598226, 2.3454024737078636, 3.1403196067223025, 3.6858556734644115, 4.034626884290841]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.0178639888763428})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.5484704971313477})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.9460361003875732})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.3041796684265137})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.4338436126708984})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.308124542236328})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.3655433654785156})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.6476149559020996})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 4.0590691566467285})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.810983657836914})
store['active_learning_steps'][37]['training']['best_epoch']=7
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.6175, 'crossentropy': 3.433427734375}
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 12064], ['id', 26133], ['id', 31947], ['id', 48151], ['id', 6314]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5637352124139456, 2.8482534330846727, 3.7737929639350494, 4.237613671989726, 4.451117392524965]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.5673828125, 'crossentropy': 2.31597900390625})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.942166328430176})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 3.296239137649536})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.382829427719116})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.834306001663208})
store['active_learning_steps'][38]['training']['best_epoch']=2
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.6002, 'crossentropy': 3.019966796875}
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 17510], ['id', 46577], ['id', 32776], ['id', 27419], ['id', 56174]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4606289070852427, 2.575248472566096, 3.387211900712818, 3.9121941045537785, 4.219400745679895]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 2.1086537837982178})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.64556884765625})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.84183931350708})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.012828826904297})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.721062660217285})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.407792091369629})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.747053384780884})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.467984676361084})
store['active_learning_steps'][39]['training']['best_epoch']=5
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.5972, 'crossentropy': 3.84700546875}
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 39522], ['id', 37629], ['id', 25558], ['id', 36337], ['id', 44993]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5158627000821254, 2.7403844028746924, 3.57126484806753, 4.070105925465041, 4.3158972632226416]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 2.0174527168273926})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.751955032348633})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.4573941230773926})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.229994297027588})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.2379183769226074})
store['active_learning_steps'][40]['training']['best_epoch']=2
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.5929, 'crossentropy': 2.9258294921875}
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 14715], ['id', 7112], ['id', 20894], ['id', 48463], ['id', 45562]], 'labels': [-1, -1, -1, -1, 8], 'scores': [1.6087788274774688, 2.730395626379936, 3.5456207208937354, 4.039050782120773, 4.317721561545656]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.2870876789093018})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.5348682403564453})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.7719593048095703})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.776665687561035})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 3.131636142730713})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.3225624561309814})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.9245445728302})
store['active_learning_steps'][41]['training']['best_epoch']=4
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.6408, 'crossentropy': 2.934423828125}
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 27920], ['id', 14164], ['id', 4683], ['id', 59365], ['id', 7852]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5740732861652935, 2.8213038185417325, 3.6536943041563115, 4.11034162924204, 4.363825425977645]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.9215507507324219})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.4357337951660156})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.1371026039123535})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.9452133178710938})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.3691539764404297})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.0370302200317383})
store['active_learning_steps'][42]['training']['best_epoch']=3
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.6216, 'crossentropy': 3.153653125}
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 25485], ['id', 42420], ['id', 36427], ['id', 45219], ['id', 14164]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.492599484820211, 2.7548190722390364, 3.650181252485435, 4.0937068759156325, 4.3508413290770855]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.0792243480682373})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.5179262161254883})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.6075258255004883})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.7577261924743652})
store['active_learning_steps'][43]['training']['best_epoch']=1
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.6132, 'crossentropy': 2.106482421875}
store['active_learning_steps'][43]['acquisition']={'indices': [['id', 21955], ['id', 31002], ['id', 14619], ['id', 175], ['id', 32793]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2585956631245074, 2.2404729560712626, 3.0008046551784, 3.5508579126996898, 3.9451748858392666]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.0468873977661133})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.554713487625122})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.987666606903076})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 3.2105181217193604})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.3986830711364746})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.422015428543091})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.2108945846557617})
store['active_learning_steps'][44]['training']['best_epoch']=4
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.6285, 'crossentropy': 3.283032421875}
store['active_learning_steps'][44]['acquisition']={'indices': [['id', 24903], ['id', 55616], ['id', 27413], ['id', 45330], ['id', 4873]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.560242228058007, 2.9041762045364585, 3.7442807048199267, 4.232046915003653, 4.438477641557716]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 2.1973013877868652})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.6845061779022217})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.9830870628356934})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.122880220413208})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.5908262729644775})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.5830812454223633})
store['active_learning_steps'][45]['training']['best_epoch']=3
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.6161, 'crossentropy': 3.1061541015625}
store['active_learning_steps'][45]['acquisition']={'indices': [['id', 14715], ['id', 39542], ['id', 25644], ['id', 29429], ['id', 1682]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5328856674860578, 2.7559582483414813, 3.623100549775967, 4.104256050682004, 4.358600718179904]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.9785845279693604})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.4463517665863037})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.629465341567993})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.166245460510254})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.7733192443847656})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.089709520339966})
store['active_learning_steps'][46]['training']['best_epoch']=3
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.6418, 'crossentropy': 2.660645703125}
store['active_learning_steps'][46]['acquisition']={'indices': [['id', 24486], ['id', 39635], ['id', 4380], ['id', 20137], ['id', 382]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.435226390430628, 2.658858267157218, 3.514830607553577, 4.013682831065042, 4.298363609175006]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.056852340698242})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.5308237075805664})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.993225574493408})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.267216920852661})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.2146754264831543})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.463470458984375})
store['active_learning_steps'][47]['training']['best_epoch']=3
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.6374, 'crossentropy': 2.9480130859375}
store['active_learning_steps'][47]['acquisition']={'indices': [['id', 21409], ['id', 48356], ['id', 53363], ['id', 14051], ['id', 44993]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5754647435166826, 2.9090292838194545, 3.788468247612421, 4.213860189072739, 4.429565968597586]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.972397804260254})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.7440476417541504})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.7074270248413086})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.3236289024353027})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.3406429290771484})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.5570549964904785})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.226750373840332})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.4181103706359863})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.6386332511901855})
store['active_learning_steps'][48]['training']['best_epoch']=6
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.6142, 'crossentropy': 3.562187890625}
store['active_learning_steps'][48]['acquisition']={'indices': [['id', 45686], ['id', 31778], ['id', 4160], ['id', 20894], ['id', 4080]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6524558786177526, 2.841270579774841, 3.704770046669392, 4.151004686903802, 4.4036437964176685]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.125854015350342})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.5371062755584717})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.7598485946655273})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.0705463886260986})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.399244785308838})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.2344255447387695})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.870105743408203})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.414220094680786})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.3995862007141113})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.2405357360839844})
store['active_learning_steps'][49]['training']['best_epoch']=7
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.6353, 'crossentropy': 3.408417578125}
store['active_learning_steps'][49]['acquisition']={'indices': [['id', 56399], ['id', 38636], ['id', 13455], ['id', 16537], ['id', 32776]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.570339247258509, 2.845567850451147, 3.680370293006355, 4.189066580686789, 4.442716166110374]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.914695382118225})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.322978973388672})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.7197179794311523})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.0709171295166016})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.057647705078125})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.965341806411743})
store['active_learning_steps'][50]['training']['best_epoch']=3
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.6338, 'crossentropy': 2.7871544921875}
store['active_learning_steps'][50]['acquisition']={'indices': [['id', 4944], ['id', 14159], ['id', 4799], ['id', 49066], ['id', 38123]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5491156149838847, 2.87066630548176, 3.685453726593698, 4.138218250570539, 4.382190515519053]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.135960102081299})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.8617002964019775})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.155897855758667})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.1595091819763184})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.394113779067993})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.3306288719177246})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.754267692565918})
store['active_learning_steps'][51]['training']['best_epoch']=4
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.6115, 'crossentropy': 3.323578125}
store['active_learning_steps'][51]['acquisition']={'indices': [['id', 51761], ['id', 55685], ['id', 57300], ['id', 14778], ['id', 11631]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.52727577946973, 2.7609121168048856, 3.6933402215536253, 4.197672699646098, 4.429236751858168]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.9659838676452637})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.3851075172424316})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.6267619132995605})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.8381032943725586})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.016634702682495})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.8202338218688965})
store['active_learning_steps'][52]['training']['best_epoch']=3
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.6228, 'crossentropy': 2.762496484375}
store['active_learning_steps'][52]['acquisition']={'indices': [['id', 12194], ['id', 7292], ['id', 25662], ['id', 34366], ['id', 33752]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5289007422157836, 2.8618567279729294, 3.6818232177603196, 4.141139997486027, 4.36490211616559]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.3180904388427734})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.4004337787628174})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.731078624725342})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.1595988273620605})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.1936702728271484})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.6544132232666016})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 4.062829971313477})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.762714147567749})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.6065893173217773})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.5649263858795166})
store['active_learning_steps'][53]['training']['best_epoch']=7
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.6057, 'crossentropy': 3.953852734375}
store['active_learning_steps'][53]['acquisition']={'indices': [['id', 29630], ['id', 7112], ['id', 48323], ['id', 36209], ['id', 35816]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5664290630555755, 2.8654834598490364, 3.671612579209846, 4.17596192555314, 4.408161297752942]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.0106353759765625})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.4865732192993164})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.8935322761535645})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.9604897499084473})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.4867146015167236})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.661064624786377})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.5707874298095703})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.5546231269836426})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.6213412284851074})
store['active_learning_steps'][54]['training']['best_epoch']=6
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.6103, 'crossentropy': 3.65886171875}
