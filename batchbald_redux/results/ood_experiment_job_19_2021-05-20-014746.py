store = {}
store['timestamp']=1621471666
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=19']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=19
store['worker_id']=19
store['num_workers']=80
store['config']={'seed': 1254, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples)) + ('FastMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 14640, 45567, 52801, 53689, 801, 55187, 26479, 50997, 3792]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.025707483291626})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 2.8455803394317627})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.998870372772217})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.4012913703918457})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.5025837421417236})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.5022788047790527})
store['active_learning_steps'][0]['training']['best_epoch']=3
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.5912, 'crossentropy': 3.263583203125}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 1.643188238143921})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.7730226516723633})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.9166687726974487})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.7016997337341309})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.7665989398956299})
store['active_learning_steps'][0]['eval_training']['best_epoch']=4
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 22191], ['id', 39008], ['id', 7949], ['id', 36171], ['id', 12046]], 'labels': [-1, -1, 5, -1, 5], 'scores': [1.1196899671991698, 1.9760468081465181, 2.5948152921867957, 2.96765196273101, 3.1573814480620848]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 2.381577491760254})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 2.840024471282959})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.516265630722046})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.45650577545166})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.9620978832244873})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.9029760360717773})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.8966846466064453})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.617619276046753})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.877941370010376})
store['active_learning_steps'][1]['training']['best_epoch']=6
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.5852, 'crossentropy': 4.246355078125}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.150902032852173})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 2.0780739784240723})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.1227259635925293})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.3733155727386475})
store['active_learning_steps'][1]['eval_training']['best_epoch']=1
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 56393], ['id', 35952], ['id', 41516], ['id', 31853], ['id', 16319]], 'labels': [-1, -1, -1, 4, 4], 'scores': [1.1103688106626537, 1.9214854328600999, 2.4634174803351967, 2.804706239711712, 3.001904617652228]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.1990742683410645})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.749850034713745})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.100109338760376})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.6784443855285645})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.246945858001709})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.395524024963379})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.8446874618530273})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 4.035193920135498})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.9490771293640137})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.3638224601745605})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.867539644241333})
store['active_learning_steps'][2]['training']['best_epoch']=8
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.607, 'crossentropy': 4.27620859375}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.8564554452896118})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.7993829250335693})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.9153735637664795})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.0594329833984375})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.94492769241333})
store['active_learning_steps'][2]['eval_training']['best_epoch']=2
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 41180], ['id', 40919], ['id', 5474], ['id', 54162], ['id', 53236]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9832414774502919, 1.7391827995377733, 2.3354088417976477, 2.64659192652564, 2.829206462918778]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.1925764083862305})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.5457613468170166})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.9616918563842773})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.4005208015441895})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.409802198410034})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.660041332244873})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.8350183963775635})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.675632953643799})
store['active_learning_steps'][3]['training']['best_epoch']=5
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6037, 'crossentropy': 3.7013046875}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.633653163909912})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.680030345916748})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.8403960466384888})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.8682096004486084})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.8527536392211914})
store['active_learning_steps'][3]['eval_training']['best_epoch']=2
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 17271], ['id', 42915], ['id', 40034], ['id', 24346], ['id', 44753]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0159389098176381, 1.8568994921681192, 2.357857034330707, 2.6804291717535373, 2.8587910497109026]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.106114625930786})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.800114393234253})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.365569591522217})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.5475263595581055})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.3767876625061035})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.774749755859375})
store['active_learning_steps'][4]['training']['best_epoch']=3
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6071, 'crossentropy': 3.4054046875}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.6397545337677002})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.651399850845337})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.649000883102417})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.5255393981933594})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.6429991722106934})
store['active_learning_steps'][4]['eval_training']['best_epoch']=4
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 49767], ['id', 28342], ['id', 17739], ['id', 36193], ['id', 20949]], 'labels': [-1, -1, -1, -1, 5], 'scores': [1.0765377534220628, 1.8281379495729317, 2.3908363460989026, 2.752007568669009, 2.9803602769403446]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 2.085425615310669})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.3064966201782227})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.052640438079834})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.5984554290771484})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.434356689453125})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.7051913738250732})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 4.012869834899902})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.218660354614258})
store['active_learning_steps'][5]['training']['best_epoch']=5
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.6006, 'crossentropy': 3.771428125}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.6881532669067383})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.9281374216079712})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.0034117698669434})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.893000841140747})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.0351479053497314})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.8285521268844604})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.9334936141967773})
store['active_learning_steps'][5]['eval_training']['best_epoch']=4
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 6351], ['id', 36578], ['id', 50679], ['id', 45076], ['id', 10924]], 'labels': [-1, -1, -1, 2, -1], 'scores': [0.9873454910100907, 1.756138994956586, 2.254561746253449, 2.6030757120603214, 2.8279206198318647]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.2853426933288574})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.8563404083251953})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.2394680976867676})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.472926616668701})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.637500762939453})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.5909, 'crossentropy': 2.9936154296875}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 1.7644450664520264})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.6066784858703613})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 1.5389106273651123})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.6655770540237427})
store['active_learning_steps'][6]['eval_training']['best_epoch']=3
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 54357], ['id', 22104], ['id', 39397], ['id', 47801], ['id', 54867]], 'labels': [-1, -1, -1, -1, 0], 'scores': [1.0809650890961613, 1.8398834017131818, 2.375437562782605, 2.7416033223420513, 2.942575132777969]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.005398988723755})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.3704910278320312})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.9686481952667236})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.1491427421569824})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.9908370971679688})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 3.0639071464538574})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.2936441898345947})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.3177781105041504})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 3.5523087978363037})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.3130197525024414})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.5004525184631348})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 3.3021087646484375})
store['active_learning_steps'][7]['training']['best_epoch']=9
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.62, 'crossentropy': 3.586259765625}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.7179336547851562})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.9686164855957031})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.853500247001648})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.9387075901031494})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.0156569480895996})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.9095721244812012})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.8739614486694336})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.927266240119934})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.078310012817383})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.9799269437789917})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.9102141857147217})
store['active_learning_steps'][7]['eval_training']['best_epoch']=11
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 27125], ['id', 34422], ['id', 27917], ['id', 4611], ['id', 54465]], 'labels': [-1, -1, -1, 0, 8], 'scores': [1.0759390959731612, 1.929707199291506, 2.5285310794093356, 2.891460840367708, 3.1646170808432457]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.0447676181793213})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.7437376976013184})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.2922751903533936})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.442044734954834})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.7823269367218018})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.952805519104004})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.8270812034606934})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.694161891937256})
store['active_learning_steps'][8]['training']['best_epoch']=5
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.5877, 'crossentropy': 4.088498046875}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 2.056739330291748})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.9395766258239746})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 2.1484601497650146})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 2.1239962577819824})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.9406914710998535})
store['active_learning_steps'][8]['eval_training']['best_epoch']=2
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 27092], ['id', 30479], ['id', 56239], ['id', 41292], ['id', 53709]], 'labels': [-1, -1, -1, -1, 4], 'scores': [1.0985710994423523, 1.772037299174987, 2.2586011436627755, 2.589345089892776, 2.752787459631864]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.1090104579925537})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.763827323913574})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.851925849914551})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.579711437225342})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.5992, 'crossentropy': 2.329791015625}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.5410484075546265})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.3557593822479248})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.3227198123931885})
store['active_learning_steps'][9]['eval_training']['best_epoch']=2
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 12461], ['id', 20647], ['id', 25580], ['id', 26229], ['id', 1555]], 'labels': [-1, -1, -1, -1, 9], 'scores': [0.8112296265635361, 1.421883292077005, 1.889869765310623, 2.2076868734463817, 2.442300687452862]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 2.1143360137939453})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.640005588531494})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.2946958541870117})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.2950053215026855})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.8483755588531494})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.802359104156494})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 4.457528114318848})
store['active_learning_steps'][10]['training']['best_epoch']=4
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.5929, 'crossentropy': 3.64344140625}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.750319004058838})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.8409380912780762})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.8529107570648193})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.0244083404541016})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.8285033702850342})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.6983968019485474})
store['active_learning_steps'][10]['eval_training']['best_epoch']=6
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 18592], ['id', 33039], ['id', 21117], ['id', 57486], ['id', 26827]], 'labels': [-1, -1, -1, 0, 1], 'scores': [0.997655593237483, 1.7688136234262828, 2.347257676525374, 2.770601112470173, 3.0433469740676733]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.2915380001068115})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.5315732955932617})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.752816915512085})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.080810546875})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.0668935775756836})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.746303081512451})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.6164965629577637})
store['active_learning_steps'][11]['training']['best_epoch']=4
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.6129, 'crossentropy': 3.293568359375}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.660374402999878})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.8548943996429443})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.819334864616394})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.8540174961090088})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.8185186386108398})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.766494870185852})
store['active_learning_steps'][11]['eval_training']['best_epoch']=5
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 52470], ['id', 11294], ['id', 23124], ['id', 14059], ['id', 20688]], 'labels': [-1, -1, -1, -1, 2], 'scores': [1.0840383543838545, 1.9141052519549184, 2.524451734790085, 2.948736391287226, 3.2646645483190397]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.023110866546631})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.5770444869995117})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.0307884216308594})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.0587081909179688})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.5920138359069824})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.301602840423584})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.7348074913024902})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.7052063941955566})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.572688341140747})
store['active_learning_steps'][12]['training']['best_epoch']=6
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.613, 'crossentropy': 3.553107421875}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.6225706338882446})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.8477551937103271})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.8869953155517578})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.8552751541137695})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.938870906829834})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.9067823886871338})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.711801528930664})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.9636731147766113})
store['active_learning_steps'][12]['eval_training']['best_epoch']=6
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 36946], ['id', 37634], ['id', 50397], ['id', 13447], ['id', 24202]], 'labels': [-1, -1, 8, -1, 3], 'scores': [0.8246291761827576, 1.5410101329906465, 2.0663100506921745, 2.3791122574680803, 2.5685300001023723]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.812201738357544})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.33046293258667})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.758857250213623})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.6575493812561035})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 3.1661276817321777})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 3.056274890899658})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.9735636711120605})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.0373759269714355})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.98508358001709})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 3.311544895172119})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 3.6785526275634766})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 3.200782060623169})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.8568432331085205})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 3.5943808555603027})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 3.735639810562134})
store['active_learning_steps'][13]['training']['best_epoch']=12
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6378, 'crossentropy': 3.449366015625}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.5463905334472656})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.7278789281845093})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.7113686800003052})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.7827043533325195})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.8078742027282715})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.767716407775879})
store['active_learning_steps'][13]['eval_training']['best_epoch']=3
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 2587], ['id', 51857], ['id', 42691], ['id', 50220], ['id', 52814]], 'labels': [-1, -1, -1, 0, -1], 'scores': [0.9000582526425275, 1.610850496301866, 2.126381998858009, 2.4186043628861182, 2.571715262412856]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.8220691680908203})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.4211649894714355})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.4529082775115967})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.92332124710083})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.0025177001953125})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.136564254760742})
store['active_learning_steps'][14]['training']['best_epoch']=3
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6336, 'crossentropy': 2.5734533203125}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.4386136531829834})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.443871021270752})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.4344892501831055})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.403023362159729})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.4868698120117188})
store['active_learning_steps'][14]['eval_training']['best_epoch']=4
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 45218], ['id', 37886], ['id', 9364], ['id', 19904], ['id', 33427]], 'labels': [-1, -1, 5, -1, 2], 'scores': [1.0659783621276069, 1.7563265589639119, 2.2918539147133346, 2.661679327988094, 2.915162345319631]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.7347018718719482})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.2300469875335693})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.4977614879608154})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.753593683242798})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.9896557331085205})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.0039687156677246})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.9586474895477295})
store['active_learning_steps'][15]['training']['best_epoch']=4
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.6372, 'crossentropy': 3.0605373046875}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.4812501668930054})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.6376233100891113})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.5676124095916748})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.5310544967651367})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.4971541166305542})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.3965144157409668})
store['active_learning_steps'][15]['eval_training']['best_epoch']=4
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 42699], ['id', 57920], ['id', 33127], ['id', 21384], ['id', 28342]], 'labels': [-1, -1, 0, 9, -1], 'scores': [1.1689320648531671, 1.865076625435991, 2.4364147411348314, 2.850510675140586, 3.078798358602854]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.621091365814209})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.1850340366363525})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.404508352279663})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.8776326179504395})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.892139434814453})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.9054760932922363})
store['active_learning_steps'][16]['training']['best_epoch']=3
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.635, 'crossentropy': 2.5899857421875}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.499884843826294})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.5458667278289795})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.5413753986358643})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.4880306720733643})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.4705164432525635})
store['active_learning_steps'][16]['eval_training']['best_epoch']=5
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 12655], ['id', 29380], ['id', 39731], ['id', 24347], ['id', 44629]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.927371768816603, 1.6470663182771497, 2.192241507344396, 2.5521305335317246, 2.804258268593977]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.6576011180877686})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.343569755554199})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.4792003631591797})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.7784945964813232})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.8317880630493164})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.7750802040100098})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.163797378540039})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.380128860473633})
store['active_learning_steps'][17]['training']['best_epoch']=5
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6199, 'crossentropy': 3.081520703125}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.7195250988006592})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.61867356300354})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.804876685142517})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.750044584274292})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.5911872386932373})
store['active_learning_steps'][17]['eval_training']['best_epoch']=2
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 10529], ['id', 59671], ['id', 40668], ['id', 49394], ['id', 32013]], 'labels': [-1, 0, -1, -1, 3], 'scores': [0.8963067671365137, 1.520973148341004, 1.986196939841434, 2.277347623622472, 2.4867533836821063]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.6009538173675537})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.4181909561157227})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.733330488204956})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.610485076904297})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.629460573196411})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.833019733428955})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.844892978668213})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.916836738586426})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 3.086240768432617})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.9652974605560303})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 3.007204294204712})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 3.488178253173828})
store['active_learning_steps'][18]['training']['best_epoch']=9
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6252, 'crossentropy': 3.569653515625}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.4778459072113037})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.9643027782440186})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.9188076257705688})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.89085853099823})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.031364917755127})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.8423197269439697})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.8624799251556396})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.7756474018096924})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.88331139087677})
store['active_learning_steps'][18]['eval_training']['best_epoch']=6
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 725], ['id', 50936], ['id', 33956], ['id', 20067], ['id', 8136]], 'labels': [-1, -1, -1, -1, 0], 'scores': [1.0365443581462488, 1.9223556000347897, 2.5501122774732146, 2.9360371067502236, 3.1188482609610806]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.7392559051513672})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.2027997970581055})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.4093456268310547})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 3.0640974044799805})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.8225746154785156})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.101539134979248})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.9953384399414062})
store['active_learning_steps'][19]['training']['best_epoch']=4
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6279, 'crossentropy': 3.0205283203125}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.509812831878662})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.7148932218551636})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.748515248298645})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.6791248321533203})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.641858458518982})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.6585140228271484})
store['active_learning_steps'][19]['eval_training']['best_epoch']=3
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 41998], ['id', 22103], ['id', 57308], ['id', 3694], ['id', 34200]], 'labels': [-1, -1, -1, 2, -1], 'scores': [1.007438697311679, 1.7361762170849144, 2.3159982384786786, 2.7861853842065702, 3.09885153905253]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.7492425441741943})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.3660149574279785})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.689908504486084})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.0110669136047363})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.076350688934326})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.05731201171875})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.726619243621826})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.471179962158203})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.045196056365967})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.7101149559020996})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.5371179580688477})
store['active_learning_steps'][20]['training']['best_epoch']=8
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.6283, 'crossentropy': 3.41492109375}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.5750927925109863})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.7107319831848145})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.7317395210266113})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.90732741355896})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.6146514415740967})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.800126314163208})
store['active_learning_steps'][20]['eval_training']['best_epoch']=3
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 7816], ['id', 7889], ['id', 28155], ['id', 19443], ['id', 34367]], 'labels': [-1, -1, -1, -1, 3], 'scores': [0.9184523281573782, 1.673269030621777, 2.2577274892793255, 2.65614122105399, 2.8856175397320385]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.64536714553833})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.211207151412964})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.653186798095703})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.7955434322357178})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.8191051483154297})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 3.0387582778930664})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.911527395248413})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 3.118945598602295})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 3.3667244911193848})
store['active_learning_steps'][21]['training']['best_epoch']=6
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.6351, 'crossentropy': 3.2205970703125}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.4680938720703125})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.85789155960083})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.9202477931976318})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.911472201347351})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.1884171962738037})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.9431555271148682})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.9600200653076172})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.051319122314453})
store['active_learning_steps'][21]['eval_training']['best_epoch']=6
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 31253], ['id', 3553], ['id', 19253], ['id', 52677], ['id', 22679]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9514937834937826, 1.687109314629077, 2.229048661930812, 2.5514307631345257, 2.742116614815278]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.7394499778747559})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.2946557998657227})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.289182186126709})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.66306734085083})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.1703367233276367})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.7231059074401855})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 3.1658339500427246})
store['active_learning_steps'][22]['training']['best_epoch']=4
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.6439, 'crossentropy': 2.738091015625}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.7249391078948975})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.8848575353622437})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.7109639644622803})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.6740055084228516})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.6071584224700928})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.624058485031128})
store['active_learning_steps'][22]['eval_training']['best_epoch']=4
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 45528], ['id', 31921], ['id', 27395], ['id', 49616], ['id', 6428]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.853709115869909, 1.4468676903614712, 1.8959058253270564, 2.245058030619835, 2.4567054360182645]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.60719633102417})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.29769229888916})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.3206748962402344})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.5320000648498535})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.822890281677246})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.961982250213623})
store['active_learning_steps'][23]['training']['best_epoch']=3
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.6432, 'crossentropy': 2.4733189453125}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.469277262687683})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.5816538333892822})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.7301783561706543})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.5195167064666748})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.5673730373382568})
store['active_learning_steps'][23]['eval_training']['best_epoch']=5
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 13185], ['id', 22876], ['id', 59032], ['id', 28467], ['id', 48280]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9939158493271155, 1.7568609119133474, 2.3377872783346225, 2.7411768748070706, 2.9665111096501686]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.4061604738235474})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.9934449195861816})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.059173107147217})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.4594204425811768})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.5388827323913574})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.96768856048584})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.5617592334747314})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6632, 'crossentropy': 2.4862693359375}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.6549510955810547})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.672424554824829})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.6199073791503906})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.8222624063491821})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.7467496395111084})
store['active_learning_steps'][24]['eval_training']['best_epoch']=2
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 56612], ['id', 10168], ['id', 35577], ['id', 20015], ['id', 5504]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0536850994055211, 1.8237239248441082, 2.355337139715502, 2.6837248133165934, 2.8735187750708]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.6143238544464111})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.0976264476776123})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.5428695678710938})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.829378128051758})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.9836983680725098})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.9190680980682373})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.8056976795196533})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 3.261826992034912})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 3.3385026454925537})
store['active_learning_steps'][25]['training']['best_epoch']=6
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.656, 'crossentropy': 2.8719634765625}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.4619959592819214})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.5347018241882324})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.5182135105133057})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.5158323049545288})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.533319115638733})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.5287692546844482})
store['active_learning_steps'][25]['eval_training']['best_epoch']=3
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 54357], ['id', 12412], ['id', 20650], ['id', 35410], ['id', 47864]], 'labels': [-1, -1, 4, -1, 5], 'scores': [0.9754116573272732, 1.7807110487574591, 2.3409930672411017, 2.726484156472279, 2.973713905722582]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.7942593097686768})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.4432144165039062})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.4344582557678223})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.711174249649048})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.726223945617676})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 3.1373167037963867})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.9556775093078613})
store['active_learning_steps'][26]['training']['best_epoch']=4
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.6401, 'crossentropy': 2.8040693359375}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.5074447393417358})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.5370376110076904})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.6593514680862427})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.6016381978988647})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.6228444576263428})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.725345253944397})
store['active_learning_steps'][26]['eval_training']['best_epoch']=6
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 13259], ['id', 12742], ['id', 38539], ['id', 48240], ['id', 48211]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.775524037086891, 1.4066858324647311, 1.8852359604315188, 2.2592830151163605, 2.5186035461417395]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.6879594326019287})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.103632926940918})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.2750353813171387})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.327627658843994})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.879638195037842})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.6419973373413086})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.7501368522644043})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.7770185470581055})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 3.0659849643707275})
store['active_learning_steps'][27]['training']['best_epoch']=6
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.6554, 'crossentropy': 2.826944921875}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.5300959348678589})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.692061185836792})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.7885351181030273})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.7150455713272095})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.7341505289077759})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.7551698684692383})
store['active_learning_steps'][27]['eval_training']['best_epoch']=3
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 17200], ['id', 48494], ['id', 31857], ['id', 47822], ['id', 39855]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.874177932830857, 1.6092681806155087, 2.2156930506738224, 2.552333003313695, 2.7956982860818784]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.471165418624878})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.972110629081726})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.523141622543335})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.561077117919922})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.780728340148926})
store['active_learning_steps'][28]['training']['best_epoch']=2
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.6387, 'crossentropy': 2.027958984375}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.397629976272583})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.4196343421936035})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.4209388494491577})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.2815630435943604})
store['active_learning_steps'][28]['eval_training']['best_epoch']=4
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 46674], ['id', 59388], ['id', 23403], ['id', 49657], ['id', 59472]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.8548832482587674, 1.4872210773016414, 1.9632713710855696, 2.2708549700204586, 2.408338843294813]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.5948805809020996})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.9783382415771484})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.426424503326416})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 3.1024632453918457})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.6088833808898926})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.1419272422790527})
store['active_learning_steps'][29]['training']['best_epoch']=3
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.646, 'crossentropy': 2.435738671875}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.4240580797195435})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.4384057521820068})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.3520910739898682})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.4430822134017944})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.3723235130310059})
store['active_learning_steps'][29]['eval_training']['best_epoch']=3
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 48010], ['id', 55341], ['id', 20200], ['id', 31796], ['id', 17248]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1346844446480853, 1.8433625232827895, 2.3266098724654762, 2.629084000256027, 2.7962120191075335]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.5677435398101807})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.894029974937439})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.291253089904785})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.6930484771728516})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.9003758430480957})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.599349021911621})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.857077121734619})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.7684805393218994})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.9796528816223145})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 3.1460764408111572})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 3.0402212142944336})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 3.12308931350708})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 3.238126039505005})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 3.007934093475342})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 3.4673287868499756})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 3.2178945541381836})
store['active_learning_steps'][30]['training']['best_epoch']=13
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.6659, 'crossentropy': 3.286546875}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.720569133758545})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.6823539733886719})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.6603580713272095})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.8070130348205566})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.671505331993103})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.7799851894378662})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.72406005859375})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.750400185585022})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.7827425003051758})
store['active_learning_steps'][30]['eval_training']['best_epoch']=6
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 4649], ['id', 27219], ['id', 36471], ['id', 25318], ['id', 51432]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1970526645020727, 2.0650431268459126, 2.7506092049479465, 3.194111207930347, 3.470004626873221]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.5613718032836914})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.8421385288238525})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.3111729621887207})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.460883617401123})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.876999855041504})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.3934688568115234})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.8955726623535156})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.9150311946868896})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.771824836730957})
store['active_learning_steps'][31]['training']['best_epoch']=6
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.6546, 'crossentropy': 2.562371875}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.5221898555755615})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.6614580154418945})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.498582124710083})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.6094810962677002})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.6002404689788818})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.4492223262786865})
store['active_learning_steps'][31]['eval_training']['best_epoch']=3
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 41545], ['id', 528], ['id', 46613], ['id', 39431], ['id', 33792]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.8913530214792976, 1.62055383732663, 2.1628827683780782, 2.5190163272104322, 2.656505681385318]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.6228747367858887})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.212791919708252})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.7082467079162598})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.3302268981933594})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.8909716606140137})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.9106709957122803})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 3.0629544258117676})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.724205255508423})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.133596420288086})
store['active_learning_steps'][32]['training']['best_epoch']=6
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.6424, 'crossentropy': 2.761901171875}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.5154826641082764})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.690643310546875})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.5375115871429443})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.467529296875})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.47648286819458})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.4567267894744873})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.65183424949646})
store['active_learning_steps'][32]['eval_training']['best_epoch']=4
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 5982], ['id', 38275], ['id', 15973], ['id', 36151], ['id', 20648]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.8454789787963417, 1.5646267481574698, 2.0588899785031574, 2.3804496950857774, 2.5691179789147025]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.512012243270874})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.1889357566833496})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.3972322940826416})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.7889046669006348})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.8425984382629395})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.7855191230773926})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.0338010787963867})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.4826412200927734})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 3.164463520050049})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.123014450073242})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 3.2840089797973633})
store['active_learning_steps'][33]['training']['best_epoch']=8
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.6431, 'crossentropy': 2.799908984375}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 1.5772099494934082})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.6789857149124146})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.720956802368164})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.6439037322998047})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.7819932699203491})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.5454912185668945})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.604009985923767})
store['active_learning_steps'][33]['eval_training']['best_epoch']=4
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 50671], ['id', 8676], ['id', 4705], ['id', 2250], ['id', 41027]], 'labels': [1, -1, 8, -1, -1], 'scores': [0.8971307044969072, 1.636981427987524, 2.214967629563858, 2.607483352647667, 2.88789032947733]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.4772977828979492})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.8469841480255127})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.2701516151428223})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.3060719966888428})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.43289852142334})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.945556402206421})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 3.33121919631958})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.679502010345459})
store['active_learning_steps'][34]['training']['best_epoch']=5
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.6671, 'crossentropy': 2.62405703125}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.509770393371582})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.5690267086029053})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.464570164680481})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.4270620346069336})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.4816854000091553})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.45826256275177})
store['active_learning_steps'][34]['eval_training']['best_epoch']=3
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 21880], ['id', 21033], ['id', 33328], ['id', 11222], ['id', 10632]], 'labels': [-1, -1, -1, -1, 9], 'scores': [0.8678225160089799, 1.5915017648851342, 2.0715515509927096, 2.409874526289287, 2.6265681015322597]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.4561809301376343})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.9014390707015991})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.152820110321045})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.2704694271087646})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.495802402496338})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.7396459579467773})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.6319150924682617})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.8734889030456543})
store['active_learning_steps'][35]['training']['best_epoch']=5
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.6803, 'crossentropy': 2.5072955078125}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.418463110923767})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.4558138847351074})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.664743185043335})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.5276806354522705})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.3864901065826416})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.4440486431121826})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.5317127704620361})
store['active_learning_steps'][35]['eval_training']['best_epoch']=4
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 48113], ['id', 23110], ['id', 17634], ['id', 43072], ['id', 30725]], 'labels': [-1, -1, -1, -1, 0], 'scores': [1.0326112149527482, 1.7593866148429251, 2.275484970274082, 2.5897320165176483, 2.77362571267816]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.4818735122680664})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.869583010673523})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.092226982116699})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.496192216873169})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.3689768314361572})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.512669563293457})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.816067695617676})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.6044158935546875})
store['active_learning_steps'][36]['training']['best_epoch']=5
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.6715, 'crossentropy': 2.4351021484375}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.4923272132873535})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.6494046449661255})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.7482337951660156})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.6255604028701782})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.712378740310669})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.6338272094726562})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.6542596817016602})
store['active_learning_steps'][36]['eval_training']['best_epoch']=7
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 20013], ['id', 27464], ['id', 40654], ['id', 5377], ['id', 16127]], 'labels': [-1, -1, -1, 5, -1], 'scores': [0.975371968042338, 1.7342846649595094, 2.334302284290054, 2.7341049902016588, 2.968727695419365]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.5997676849365234})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.061858892440796})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.54343318939209})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.6170144081115723})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.7387678623199463})
store['active_learning_steps'][37]['training']['best_epoch']=2
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.644, 'crossentropy': 2.1585892578125}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.477079153060913})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.4222490787506104})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.3671636581420898})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.3776277303695679})
store['active_learning_steps'][37]['eval_training']['best_epoch']=4
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 36247], ['id', 9660], ['id', 1987], ['id', 27328], ['id', 56009]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.8725706234328876, 1.5274603679750691, 2.0094525553926124, 2.3205249446348777, 2.4607864460681865]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.4855767488479614})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.0017411708831787})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.2638192176818848})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.2599682807922363})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.503054618835449})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.7212307453155518})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.0182695388793945})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.489537000656128})
store['active_learning_steps'][38]['training']['best_epoch']=5
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.6641, 'crossentropy': 2.6857005859375}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.3622410297393799})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.496478796005249})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.5132107734680176})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.5122771263122559})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.4419782161712646})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.4862440824508667})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.3825175762176514})
store['active_learning_steps'][38]['eval_training']['best_epoch']=6
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 30037], ['id', 27258], ['id', 28615], ['id', 22550], ['id', 3895]], 'labels': [-1, -1, 1, -1, 8], 'scores': [0.9976057652237165, 1.7860537194308228, 2.3580193453229072, 2.78026723940836, 3.0216185181893493]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.4336655139923096})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.814874529838562})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.248600482940674})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.309143304824829})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.41182541847229})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.468871593475342})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.7042317390441895})
store['active_learning_steps'][39]['training']['best_epoch']=4
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.6635, 'crossentropy': 2.6309423828125}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.4871253967285156})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.6763280630111694})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.7086923122406006})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.6132224798202515})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.5736711025238037})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.6178550720214844})
store['active_learning_steps'][39]['eval_training']['best_epoch']=4
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 4664], ['id', 41937], ['id', 42387], ['id', 18040], ['id', 18598]], 'labels': [-1, -1, -1, -1, 5], 'scores': [0.958606176225782, 1.7355627648309204, 2.3135794892416843, 2.671747010987007, 2.8751753231909327]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.412885069847107})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.89119291305542})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.233950614929199})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.1214210987091064})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.4811863899230957})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.571169137954712})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.6074776649475098})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.5679931640625})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.5539679527282715})
store['active_learning_steps'][40]['training']['best_epoch']=6
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.665, 'crossentropy': 2.8477638671875}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.4026305675506592})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.6087908744812012})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.912400722503662})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.7865266799926758})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.7691179513931274})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.835008978843689})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.7259052991867065})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.8197393417358398})
store['active_learning_steps'][40]['eval_training']['best_epoch']=8
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 17644], ['id', 37526], ['id', 5398], ['id', 23433], ['id', 22835]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1128857348915169, 1.9238442503914697, 2.5842738266282574, 3.0334526148404817, 3.241914458154735]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.4488526582717896})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.8679481744766235})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.239011287689209})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.443377733230591})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.4083945751190186})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.617650032043457})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.910205841064453})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.7835466861724854})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.5554962158203125})
store['active_learning_steps'][41]['training']['best_epoch']=6
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.6616, 'crossentropy': 2.8471841796875}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.3460180759429932})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.5024739503860474})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.5358898639678955})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.4822907447814941})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.4514095783233643})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.4712493419647217})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.6016154289245605})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.4590110778808594})
store['active_learning_steps'][41]['eval_training']['best_epoch']=5
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 4809], ['id', 17644], ['id', 31188], ['id', 56224], ['id', 48102]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0274144391188484, 1.750688948892119, 2.2817906416682066, 2.6953970710188524, 2.9690888059641454]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.4828436374664307})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.780989646911621})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.178208827972412})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.3813235759735107})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.242593765258789})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.4767441749572754})
store['active_learning_steps'][42]['training']['best_epoch']=3
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.6685, 'crossentropy': 2.3668232421875}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.3712414503097534})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.4614810943603516})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.5174212455749512})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.4461561441421509})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.425185203552246})
store['active_learning_steps'][42]['eval_training']['best_epoch']=3
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 25748], ['id', 54357], ['id', 6171], ['id', 4050], ['id', 25948]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9854359841820893, 1.7193090436114686, 2.218635246777438, 2.6026997894770814, 2.8485817135962166]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.5115915536880493})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.699842929840088})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.8852161169052124})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.335235834121704})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.5436391830444336})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.4014580249786377})
store['active_learning_steps'][43]['training']['best_epoch']=3
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.6709, 'crossentropy': 2.027083203125}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.3169739246368408})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.3006035089492798})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.1820766925811768})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.2379709482192993})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.1796406507492065})
store['active_learning_steps'][43]['eval_training']['best_epoch']=4
store['active_learning_steps'][43]['acquisition']={'indices': [['id', 42597], ['id', 59742], ['id', 31326], ['id', 17076], ['id', 33294]], 'labels': [-1, -1, -1, 8, -1], 'scores': [1.0840094071386899, 1.7787474214948236, 2.333082771960546, 2.6868931085726624, 2.9057489983540776]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.50082266330719})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.125326633453369})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.1687498092651367})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.354796886444092})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.6976571083068848})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.6331300735473633})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.979893922805786})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.4481239318847656})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.6675100326538086})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.6972570419311523})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.9923057556152344})
store['active_learning_steps'][44]['training']['best_epoch']=8
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.6702, 'crossentropy': 2.667300390625}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.4499527215957642})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.4147828817367554})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.4062185287475586})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.474100112915039})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.389295220375061})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.387073040008545})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.363725185394287})
store['active_learning_steps'][44]['eval_training']['best_epoch']=4
store['active_learning_steps'][44]['acquisition']={'indices': [['id', 804], ['id', 24108], ['id', 30311], ['id', 34385], ['id', 18651]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9812961804015445, 1.756706895872398, 2.3336535335084103, 2.729851867855338, 2.980364663335752]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.3979871273040771})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.031247615814209})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.882861852645874})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.139226198196411})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.536020517349243})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.2621941566467285})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.4995741844177246})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.8888440132141113})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.668026924133301})
store['active_learning_steps'][45]['training']['best_epoch']=6
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.6562, 'crossentropy': 2.5763275390625}
store['active_learning_steps'][45]['eval_training']={}
store['active_learning_steps'][45]['eval_training']['epochs']=[]
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.4850493669509888})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.5541141033172607})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.6519355773925781})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.7122716903686523})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.470874547958374})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.4645028114318848})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.5067596435546875})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.4929614067077637})
store['active_learning_steps'][45]['eval_training']['best_epoch']=7
store['active_learning_steps'][45]['acquisition']={'indices': [['id', 37788], ['id', 58390], ['id', 19416], ['id', 7222], ['id', 12784]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2432365494462823, 2.2250569234417417, 2.975495818345043, 3.4235969655027882, 3.65405006104869]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.5467443466186523})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.740278959274292})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.1188483238220215})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.443079948425293})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.548128128051758})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.517754077911377})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.8244175910949707})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.8304409980773926})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.6035807132720947})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.664719343185425})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.9603819847106934})
store['active_learning_steps'][46]['training']['best_epoch']=8
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.6919, 'crossentropy': 2.8651158203125}
store['active_learning_steps'][46]['eval_training']={}
store['active_learning_steps'][46]['eval_training']['epochs']=[]
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.327641248703003})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.4933905601501465})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.6287513971328735})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.6242446899414062})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.5109623670578003})
store['active_learning_steps'][46]['eval_training']['best_epoch']=2
store['active_learning_steps'][46]['acquisition']={'indices': [['id', 51314], ['id', 40308], ['id', 8342], ['id', 49448], ['id', 37262]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.081575693518111, 2.001174126709606, 2.6015120145834993, 2.9912859308426327, 3.1691966845583543]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.4340229034423828})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.9161649942398071})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.1237382888793945})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.0363411903381348})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.295515537261963})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.4905612468719482})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.733231544494629})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.610807180404663})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.834923028945923})
store['active_learning_steps'][47]['training']['best_epoch']=6
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.6831, 'crossentropy': 2.5348244140625}
store['active_learning_steps'][47]['eval_training']={}
store['active_learning_steps'][47]['eval_training']['epochs']=[]
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.3444738388061523})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.5915091037750244})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.5228796005249023})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.6244500875473022})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.8499598503112793})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.6374313831329346})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.5991718769073486})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.6087329387664795})
store['active_learning_steps'][47]['eval_training']['best_epoch']=7
store['active_learning_steps'][47]['acquisition']={'indices': [['id', 19110], ['id', 36504], ['id', 30798], ['id', 2019], ['id', 23814]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9867065479480341, 1.7490812376791625, 2.300935260589282, 2.6908356503224953, 2.9578378920764896]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.454679250717163})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.802499771118164})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.1385903358459473})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.287418842315674})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.429617404937744})
store['active_learning_steps'][48]['training']['best_epoch']=2
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.6642, 'crossentropy': 1.8723279296875}
store['active_learning_steps'][48]['eval_training']={}
store['active_learning_steps'][48]['eval_training']['epochs']=[]
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.2484321594238281})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.1959646940231323})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.1923589706420898})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.1607983112335205})
store['active_learning_steps'][48]['eval_training']['best_epoch']=3
store['active_learning_steps'][48]['acquisition']={'indices': [['id', 18135], ['id', 20597], ['id', 58166], ['id', 17491], ['id', 28559]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.8233686986002886, 1.4637309656450044, 1.903011445784435, 2.1846123532514223, 2.386115992641124]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.5916411876678467})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.697180986404419})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.0447938442230225})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.3257651329040527})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.456756114959717})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.5191216468811035})
store['active_learning_steps'][49]['training']['best_epoch']=3
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.664, 'crossentropy': 2.2181267578125}
store['active_learning_steps'][49]['eval_training']={}
store['active_learning_steps'][49]['eval_training']['epochs']=[]
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.4656414985656738})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.3694740533828735})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.3547663688659668})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.4484564065933228})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.4800684452056885})
store['active_learning_steps'][49]['eval_training']['best_epoch']=3
store['active_learning_steps'][49]['acquisition']={'indices': [['id', 48866], ['id', 16532], ['id', 57184], ['id', 22546], ['id', 13305]], 'labels': [-1, -1, -1, 5, 3], 'scores': [0.6682185506649116, 1.2537359679096411, 1.718778312695052, 2.0614114155255887, 2.2503569961350554]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.540473461151123})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.8220287561416626})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.1551432609558105})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.712196111679077})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.3285250663757324})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.966839551925659})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.7782506942749023})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.7820944786071777})
store['active_learning_steps'][50]['training']['best_epoch']=5
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.654, 'crossentropy': 2.4416755859375}
store['active_learning_steps'][50]['eval_training']={}
store['active_learning_steps'][50]['eval_training']['epochs']=[]
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.3436264991760254})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.4895474910736084})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.5082509517669678})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.4630964994430542})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.513805627822876})
store['active_learning_steps'][50]['eval_training']['best_epoch']=2
store['active_learning_steps'][50]['acquisition']={'indices': [['id', 23138], ['id', 27427], ['id', 7160], ['id', 14109], ['id', 30553]], 'labels': [-1, -1, -1, -1, 5], 'scores': [0.7138822371945974, 1.3875415889028697, 1.8651249103127077, 2.157152520960765, 2.352982122298221]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.4680094718933105})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.8682785034179688})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.0997860431671143})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.2977800369262695})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.6413087844848633})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.8203608989715576})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.532999038696289})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.9149742126464844})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 3.0468709468841553})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.7778663635253906})
store['active_learning_steps'][51]['training']['best_epoch']=7
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.6595, 'crossentropy': 2.834752734375}
store['active_learning_steps'][51]['eval_training']={}
store['active_learning_steps'][51]['eval_training']['epochs']=[]
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.3491941690444946})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.4733390808105469})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.564941644668579})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.5890172719955444})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.53461754322052})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.4867792129516602})
store['active_learning_steps'][51]['eval_training']['best_epoch']=3
store['active_learning_steps'][51]['acquisition']={'indices': [['id', 26028], ['id', 24095], ['id', 9348], ['id', 55160], ['id', 45010]], 'labels': [2, -1, -1, 9, 2], 'scores': [0.7436827475677741, 1.3977056492724638, 1.9156587380645664, 2.2450736520165044, 2.451691700756709]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.576171875, 'crossentropy': 1.6477309465408325})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.8948395252227783})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.2531867027282715})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.3587207794189453})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.311140537261963})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.8238332271575928})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.8554184436798096})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.928279399871826})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 3.245246410369873})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.897228717803955})
store['active_learning_steps'][52]['training']['best_epoch']=7
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.6602, 'crossentropy': 3.11426640625}
store['active_learning_steps'][52]['eval_training']={}
store['active_learning_steps'][52]['eval_training']['epochs']=[]
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.446563720703125})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.5720094442367554})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.8858600854873657})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.919880747795105})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.8512914180755615})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.9161717891693115})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.750478744506836})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.8731807470321655})
store['active_learning_steps'][52]['eval_training']['best_epoch']=5
store['active_learning_steps'][52]['acquisition']={'indices': [['id', 16894], ['id', 13520], ['id', 36152], ['id', 18637], ['id', 4768]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.8504712148930104, 1.5947960520477444, 2.175719156818961, 2.5580817411362795, 2.8079680619720886]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.5050690174102783})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.8865561485290527})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.147351026535034})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.2690696716308594})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.348510503768921})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.8140625953674316})
store['active_learning_steps'][53]['training']['best_epoch']=3
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.6673, 'crossentropy': 2.2175283203125}
store['active_learning_steps'][53]['eval_training']={}
store['active_learning_steps'][53]['eval_training']['epochs']=[]
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.41619873046875})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.4799752235412598})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.3472044467926025})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.3990424871444702})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.3002264499664307})
store['active_learning_steps'][53]['eval_training']['best_epoch']=4
store['active_learning_steps'][53]['acquisition']={'indices': [['id', 43378], ['id', 15140], ['id', 22519], ['id', 39272], ['id', 3224]], 'labels': [-1, -1, 5, 0, 4], 'scores': [0.8367609154940665, 1.4445258616042025, 1.906840856629941, 2.274711902907146, 2.4970123972474285]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 1.567894458770752})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.7875107526779175})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.312112808227539})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.3624587059020996})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.882190465927124})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.52897310256958})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.879004955291748})
store['active_learning_steps'][54]['training']['best_epoch']=4
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.6455, 'crossentropy': 2.6320134765625}
